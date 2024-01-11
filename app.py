from flask import Flask, render_template,request
import os
import pickle
import pandas as pd
import requests
import ast
import numpy as np


# TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('D:/MOVIE RECOMMENDED SYSTEM/templates/static')

# trending_Movies=pickle.load(open('trending_Movies.pkl','rb'))
trending_Movies = pd.read_pickle('trending_Movies.pkl') 
Popular_Movies = pd.read_pickle('Popular_Movies.pkl')
# movies = pd.read_csv('tmdb_5000_movies.csv')
movies = pd.read_pickle('TotalMovies.pkl')
cosine_sim = pd.read_pickle('cosine_sim.pkl')
tags_sim = pd.read_pickle('tags.pkl')
indices = pd.read_pickle('indices.pkl')



Collabrative_df_movies = pd.read_pickle('Collabrative_df_movies.pkl')
Collabrative_pt = pd.read_pickle('Collabrative_pt')
Collabrative_similarity_scores = pd.read_pickle('Collabrative_similarity_scores.pkl')





# app = Flask(__name__)
app = Flask(__name__, static_folder=STATIC_DIR)




def fetchposter(movieid):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movieid}?api_key=d458735f25ecb08494fc48031a0bde63&language=en-US')
    
    if response.status_code == 200:
        data = response.json()

        # Check if 'poster_path' key exists in the response
        if 'poster_path' in data:
            return "https://image.tmdb.org/t/p/w185/" + data["poster_path"]
        else:
            return "Poster path not found in the response"
    else:
        return f"Error: {response.status_code} - {response.text}"

def fetch_imdb_poster(movieid):
    url = "https://imdb8.p.rapidapi.com/title/get-images"
    querystring = {"tconst": movieid, "limit": "25"}
    headers = {
        "X-RapidAPI-Key": "46f65b13a1msh93aa905d2fc2d1ep107de1jsncaa5a390e9c6",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        if 'url' in data:
            # Assuming you want the URL of the first poster
            first_poster_url = data['url'][0].get('url', "Poster URL not found")
            return first_poster_url
        else:
            return "Posters not found in the response"
    else:
        return f"Error: {response.status_code} - {response.text}"






posterpath=[]
PopularMoviePosterPath=[]

for i in list(trending_Movies.head(12)['id'].values):
  posterpath.append(fetchposter(i))

for i in list(Popular_Movies.head(5)['id'].values):
  PopularMoviePosterPath.append(fetchposter(i))





    
# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, cosine_sim,movies):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:13]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return movies[['title','id',"vote_average",'homepage','vote_count','genres']].iloc[movie_indices]


def recommendMoviesUsingCollabrative(movie_name):
    # index fetch
    index = np.where(Collabrative_pt.index==movie_name)[0][0]
    similar_items = sorted(list(enumerate(Collabrative_similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:12]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = Collabrative_df_movies[Collabrative_df_movies['title'] == Collabrative_pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('title')['title'].values))
        item.extend(list(temp_df.drop_duplicates('title')['vote_count'].values))
        item.extend(list(temp_df.drop_duplicates('title')['vote_average'].values))
        item.extend(list(temp_df.drop_duplicates('title')['genres'].values))
        item.extend(list(temp_df.drop_duplicates('title')['homepage'].values))
        item.extend(list(temp_df.drop_duplicates('title')['imdb_id'].values))
        
        data.append(item)
    
    return data







@app.route('/')
def home():
    return render_template('index.html',
                           
                           popTitle=list(Popular_Movies.head(5)['title'].values),
                           popVoteAverage=list(Popular_Movies.head(5)['vote_average'].values),
                           popOverview=list(Popular_Movies.head(5)['overview'].values),
                           popGenre=[movie[:2] for movie in Popular_Movies["genres"].head(5)],
                           PosterPath=PopularMoviePosterPath,
                           ReleaseYear=list(Popular_Movies.head(5)['release_date'].values),
                           methods=['GET', 'POST'])

@app.route('/movies')
def movies():
    return render_template('movies.html',
                           movieName=list(trending_Movies.head(12)['title'].values),
                           VoteAverage=list(trending_Movies.head(12)['vote_average'].values),
                           MovieID=list(trending_Movies.head(12)['id'].values),
                           VoteCount=list(trending_Movies.head(12)['vote_count'].values),
                           Homepage=list(trending_Movies.head(12)['homepage'].values),
                           PosterPath=posterpath
                           )




@app.route('/search', methods=['GET', 'POST'])
def search():
    movies = pd.read_pickle('TotalMovies.pkl')
    if request.method == 'POST':
        query = request.form['search']
        result = get_recommendations(query,cosine_sim,movies)
        ContentBasedPoster=[]
        for i in result['id'].values:
         ContentBasedPoster.append(fetchposter(i))
        return render_template('index.html', MovieTitle=result['title'].values,
                                            MovieVote=result['vote_average'].values,
                                            MovieHomepage=result['homepage'].values,
                                            MovieVoteCount=result['vote_count'].values,
                                            MoviePoster=ContentBasedPoster,
                               )
    return render_template('index.html')    



@app.route('/searchbytags', methods=['GET', 'POST'])
def searchbytags():
    movies = pd.read_pickle('TotalMovies.pkl')
    if request.method == 'POST':
        query = request.form['searchbytags']
        result = get_recommendations(query,tags_sim,movies)
        TagsBasedPoster=[]
        for i in result['id'].values:
         TagsBasedPoster.append(fetchposter(i))
        return render_template('index.html', TagsTitle=result['title'].values,
                                             TagsGenre=[movie[:2] for movie in result["genres"]],
                                             TagsPoster=TagsBasedPoster,
                                            
                               )
    return render_template('index.html')    

@app.route('/searchbycollabrativefiltering', methods=['GET', 'POST'])
def searchbycollabrativefiltering():
    movies = pd.read_pickle('TotalMovies.pkl')
    if request.method == 'POST':
        query = request.form['searchbycollabrativefiltering']
        result = recommendMoviesUsingCollabrative(query)
        # TagsBasedPoster=[]
        # for i in result[5]:
        #  TagsBasedPoster.append(fetch_imdb_poster(i))
        return render_template('index.html', result1=result[:5],
                                             result2=result[5:],
                                            #  poster=TagsBasedPoster
                                        )
    return render_template('index.html') 






if __name__ == '__main__':
    app.run(debug=True)

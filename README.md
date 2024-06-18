🎬 Embark on a Cinematic Journey with Our Movie Recommender System! 🚀🍿

Thrilled to unveil the culmination of months of hard work and passion - our Movie Recommender System 🌟

There are basically three types of recommender systems:-

 -   Demographic Filtering- They offer generalized recommendations to every user, based on movie popularity and/or genre. The System recommends the same movies to users with similar demographic features. Since each user is different , this approach is considered to be too simple. The basic idea behind this system is that movies that are more popular and critically acclaimed will have a higher probability of being liked by the average audience.

 -   Content Based Filtering- They suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person liked a particular item, he or she will also like an item that is similar to it.

 -   Collaborative Filtering- This system matches persons with similar interests and provides recommendations based on this matching. Collaborative filters do not require item metadata like its content-based counterparts.
 It is basically of two types:

1. User Based Collaborative Filtering
      Collaborative filtering is making recommend according to combination of your experience and experiences of other people.
First we need to make user vs item matrix.
    - Each row is users and each columns are items like movie, product or websites
Secondly, computes similarity scores between users.
    - Each row is users and each row is vector.
    -  Compute similarity of these rows (users).
  
Thirdly, find users who are similar to you based on past behaviours
Finally, it suggests that you are not experienced before.

Lets make an example of user based collaborative filtering
     Think that there are two people
     First one watched 2 movies that are lord of the rings and hobbit
     Second one watched only lord of the rings movie
     User based collaborative filtering computes similarity of these two people and sees both are watched a lord of the rings.
     Then it recommends hobbit movie to second one as it can be seen picture


![Image](https://preview.ibb.co/feq3EJ/resim_a.jpg)


User based collaborative filtering has some problems

     - In this system, each row of matrix is user. Therefore, comparing and finding similarity between of them is computationaly hard and spend too much computational power.
     - Also, habits of people can be changed. Therefore making correct and useful recommendation can be hard in time.
In order to solve these problems, lets look at another recommender system that is item based collaborative filtering


2. Item Based Collaborative Filtering 
      In this system, instead of finding relationship between users, used items like movies or stuffs are compared with each others.
      In user based recommendation systems, habits of users can be changed. This situation makes hard to recommendation. However, in item based recommendation systems, movies or stuffs does not change. Therefore recommendation is easier.
      On the other hand, there are almost 7 billion people all over the world. Comparing people increases the computational power. However, if items are compared, computational power is less.
   
      In item based recommendation systems, we need to make user vs item matrix that we use also in user based recommender systems.
            Each row is user and each column is items like movie, product or websites.
            However, at this time instead of calculating similarity between rows, we need to calculate similarity between columns that are items like movies or stuffs.
Lets look at how it is works.
   - Firstly, there are similarities between lord of the rings and hobbit movies because both are liked by three different people. There is a similarity point between these two movies.
   - If the similarity is high enough, we can recommend hobbit to other people who only watched lord of the rings movie as it can be seen in figure below.
  

![Image](https://image.ibb.co/maEQdd/resim_b.jpg)

I created recommenders using demographic , content- based and collaborative filtering. While demographic filtering is very elemantary and cannot be used practically, Hybrid Systems can take advantage of content-based and collaborative filtering as the two approaches are proved to be almost complimentary. 


🛠️ Behind the Scenes:
Data Collection: We've sourced a massive dataset from The Movie Database (TMDB) to build our recommendation engine's core.📊

Data Preprocessing: Our process involves thorough data cleaning to ensure our information is accurate, complete, and relevant. This meticulous groundwork is critical to building a reliable system. 🧹

Model Development: The engine uses advanced methods, like stemming to get to the root of words, the Bag of Words approach for feature extraction, managing stop words for efficiency, and cosine similarity to determine movie similarity. This sophisticated setup allows us to offer accurate and personalized movie recommendations. 🤖

TMDB API Integration: To enhance the user experience, we've integrated the TMDB API to fetch stunning movie posters, adding visual appeal and helping users make informed movie choices. 🎨

Website Creation with Flask: Our user interface is built with Flask, providing an intuitive and interactive platform for users to explore personalized movie suggestions. 


🚀 How It Works:
Select a favorite movie, like "Iron Man 2."

Our system delves into genres, cast, crew, and keywords for a holistic understanding.

Cosine Similarity computes the magic, suggesting movies with resonant content.

Dynamic Posters from TMDb make the entire experience visually immersive.

🌟 Key Outcomes:
Personalized Recommendations tailored to your unique taste.

An Interactive Interface crafted on Flask for an intuitive user experience.

💻 Tech Stack:
Python, Pandas, Scikit-Learn, Flask, TMDb API

📈 Results:
Successful in delivering spot-on movie recommendations, heightening user engagement and satisfaction.

This project was a collaborative effort with my talented teammate Ahsan Sajjad. Together, we implemented cutting-edge features to create an engaging and innovative movie recommendation system

🌟 Explore the Full Code and Project Details on GitHub: 

Dive into the world of cinema, experiment with your favorite movies, and share your thoughts! 🚀🍿

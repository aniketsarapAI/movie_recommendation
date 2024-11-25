# Recommendation-systems
Recommendation Systems
In today’s fast-paced world, recommendation systems play a crucial role in simplifying decision-making by helping users discover relevant content quickly and efficiently. These systems alleviate the cognitive load associated with sifting through countless options, enabling individuals to make informed choices seamlessly.

A recommendation system leverages Artificial Intelligence (AI) algorithms to analyze user behavior and preferences, generating personalized content recommendations. By utilizing factors such as user profiles, search and browsing history, and the behavior of similar users, these systems curate customized lists of items that are highly relevant and engaging.

This is achieved using predictive modeling and advanced heuristics, which process the available data to identify patterns and deliver tailored recommendations. Such AI-driven solutions enhance user experiences and drive engagement, making them indispensable in domains like entertainment, e-commerce, and content discovery.


## Demo of Movie Recommendation  

![](https://github.com/aniketsarapAI/movie_recommendation/blob/main/demo.gif)


## About This Project
This is a Streamlit-based web application designed to recommend movies tailored to user preferences. By analyzing user input, the application suggests similar movies to enhance the discovery experience.

## Dataset
The dataset used in this application is included within the project repository and supports the generation of personalized movie recommendations. [dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## How to run the project
Clone the repository
```bash
https://github.com/aniketsarapAI/movie_recommendation.git
```

Create conda enviornment after creating repository
```bash
conda create -n movie python=3.7.10 -y
conda activate movie
```
install requirements
```bash
pip install -r requirements.txt
```
run jupyter notebook
```bash
recommender Systems.ipynb
```
This will result in creation of 2 files
```bash
movie_list.pkl
similarity.pkl
```

run streamlit app
```bash
streamlit run app.py
```

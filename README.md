# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Streamlit, and Machine Learning**.  
The application recommends movies similar to the movie selected by the user based on movie features and similarity scores.

## 🚀 Live Demo

🔗 Coming soon...

## 📌 Project Overview

This project is a **content-based recommendation system** that suggests movies similar to a movie selected by the user.

The system uses **text vectorization and cosine similarity** to calculate how similar movies are to each other. The application is built with **Streamlit** to provide an interactive user interface.

Movie posters, ratings, and other movie information are fetched using the **TMDB API**.

## ✨ Features

- 🎬 Select a movie from the available movie collection
- 🤖 Get recommendations for similar movies
- 🔍 Content-based recommendation using similarity
- 📊 Uses vectorization and cosine similarity
- 🖼️ Displays movie posters
- ⭐ Displays movie ratings
- 🌐 Fetches movie information using TMDB API
- 💻 Interactive Streamlit web application

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **Requests**
- **Scikit-learn**
- **Pickle**
- **TMDB API**

## 🧠 How It Works

The recommendation system follows these main steps:

### 1. Data Collection

The project uses the **TMDB 5000 Movies Dataset** containing information about movies such as:

- Movie title
- Genres
- Keywords
- Cast
- Crew
- Overview

### 2. Feature Processing

Relevant movie information is combined to create a feature representation for each movie.

### 3. Vectorization

The textual movie features are converted into numerical vectors using **vectorization**.

### 4. Similarity Calculation

**Cosine Similarity** is used to calculate the similarity between movies.

The similarity score determines how closely related two movies are.

### 5. Recommendation

When a user selects a movie:

1. The selected movie is located in the dataset.
2. Its similarity scores with other movies are retrieved.
3. Movies are sorted according to their similarity.
4. The most similar movies are recommended.

### 6. Movie Details

The **TMDB API** is used to retrieve movie posters and additional movie information.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── MovieRecommenderSystem.ipynb
├── movies.pkl
├── cos_similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── .gitignore
└── .gitattributes

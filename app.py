import streamlit as st
import pandas as pd
import pickle
import requests
import time


# =========================
# TMDB CONFIGURATION
# =========================

API_KEY = st.secrets["TMDB_API_KEY"]

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# =========================
# LOAD MODEL / DATA
# =========================

cos_similarity = pickle.load(
    open("cos_similarity.pkl", "rb")
)

m = pickle.load(
    open("movies.pkl", "rb")
)

m_list = m["title"].values.tolist()


# =========================
# RECOMMENDATION FUNCTION
# =========================

def recommendation(movie):

    movie_index = m[m["title"] == movie].index[0]

    distances = cos_similarity[movie_index]

    lt = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    r_movies = []

    for j in lt:

        movie_name = m.iloc[j[0]].title

        r_movies.append(movie_name)

    return r_movies


# =========================
# FETCH MOVIE FROM TMDB
# =========================

@st.cache_data
def fetch(movie):

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie,
        "language": "en-US"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])

        if not results:
            return None

        return results[0]

    except requests.exceptions.RequestException:

        return None


# =========================
# POSTER URL
# =========================

def poster_url(path):

    if path:

        return IMAGE_URL + path

    return None


# =========================
# STREAMLIT UI
# =========================

st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and get 5 similar movie recommendations."
)


option = st.selectbox(
    "Select a movie",
    m_list
)


# =========================
# RECOMMEND BUTTON
# =========================

if st.button("Recommend"):

    recommendations = recommendation(option)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i, movie_name in enumerate(recommendations):

        # Small delay between TMDB requests
        time.sleep(0.5)

        movie = fetch(movie_name)

        with cols[i]:

            # -------------------------
            # If TMDB request failed
            # -------------------------

            if movie is None:

                st.write(movie_name)

                st.caption(
                    "TMDB information unavailable"
                )

                continue


            # -------------------------
            # POSTER
            # -------------------------

            poster = poster_url(
                movie.get("poster_path")
            )

            if poster:

                st.image(
                    poster,
                    use_container_width=True
                )

            else:

                st.write(
                    "No poster available"
                )


            # -------------------------
            # MOVIE TITLE
            # -------------------------

            st.markdown(
                f"**{movie.get('title', movie_name)}**"
            )


            # -------------------------
            # RATING
            # -------------------------

            rating = movie.get(
                "vote_average",
                0
            )

            st.write(
                f"⭐ {rating:.1f}/10"
            )


            # -------------------------
            # RELEASE DATE
            # -------------------------

            release_date = movie.get(
                "release_date",
                "Unknown"
            )

            st.write(
                f"📅 {release_date}"
            )


            # -------------------------
            # OVERVIEW
            # -------------------------

            overview = movie.get(
                "overview",
                ""
            )

            if overview:

                with st.expander("Overview"):

                    st.write(overview)

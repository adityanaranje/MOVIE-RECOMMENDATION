# Import required libraries.
import streamlit as st
import pickle
import pandas as pd
import requests
import base64


# Set background of api
bg = "static/movie.jfif"
bg_ext = "jfif"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{bg_ext};base64,{base64.b64encode(open(bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)



# Function to fetch posters of recommended movies from website
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=<<your_api_key>>&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500"+data['poster_path']


# Function to get the recommendations from given input
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Get movies data which is stored as pickle file
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Get similarity pickle file which is based on cosine distance
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Set title of Api
st.title('Movie Recommender System')

# Set selection box
selected = st.selectbox('Select Movie', (movies['title'].values))

# Recommendation button
if st.button('Recommend'):
    name, posters = recommend(selected)

    col1, col2, col3, col4, col5 = st.columns(5)

    
    # Showing recommended movie names with their posters.
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])


st.text('Created By-Aditya Naranje')

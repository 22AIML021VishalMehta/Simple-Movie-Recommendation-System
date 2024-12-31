import streamlit as st
import pandas as pd
import joblib

data = pd.read_csv('Data/LargeMovieDataset.csv')
kmeans = joblib.load('Model/movie_clustering_model.pkl')

# Assign clusters dynamically
def assign_clusters(data):
    """
    Assigns clusters to the dataset dynamically using the trained KMeans model.
    """
    feature_columns = ['Rating', 'Popularity']  # Features used in clustering
    X = data[feature_columns]
    data['Cluster'] = kmeans.predict(X)
    return data

# Recommendation function
def recommend_movies(movie_title, num_recommendations=5):
    """
    Recommends movies similar to the input movie based on clustering.
    """
    clustered_data = assign_clusters(data)

    if movie_title not in clustered_data['Title'].values:
        return None, f"The movie '{movie_title}' is not in the dataset."

    movie_cluster = clustered_data[clustered_data['Title'] == movie_title]['Cluster'].iloc[0]

    similar_movies = clustered_data[clustered_data['Cluster'] == movie_cluster]

    similar_movies = similar_movies[similar_movies['Title'] != movie_title]

    num_recommendations = min(num_recommendations, len(similar_movies))

    recommendations = similar_movies.sample(num_recommendations)['Title'].tolist()

    return recommendations, None

st.title("🎥 Simple Movie Recommendation System")
st.write("Enter the name of a movie, and we'll recommend similar movies.")

movie_name = st.text_input("Enter a movie title:", placeholder="E.g., Inception")

if st.button("Get Recommendations"):
    if movie_name.strip():
        recommendations, error = recommend_movies(movie_name.strip())
        if error:
            st.error(error)
        else:
            st.subheader(f"Movies similar to '{movie_name}':")
            for rec in recommendations:
                st.write(f"- {rec}")
    else:
        st.warning("Please enter a valid movie title!")

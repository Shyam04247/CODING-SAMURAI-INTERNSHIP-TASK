import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print("Movies Dataset:")
print(movies.head())

print("\nRatings Dataset:")
print(ratings.head())
# Calculate average rating for each movie
average_ratings = ratings.groupby("movieId")["rating"].mean()

# Convert to dataframe
average_ratings = average_ratings.reset_index()

# Merge with movie titles
popular_movies = pd.merge(average_ratings, movies, on="movieId")

# Sort by rating (highest first)
popular_movies = popular_movies.sort_values(by="rating", ascending=False)

print("\nTop Rated Movies:")
print(popular_movies[["title", "rating"]].head(10))

movie_stats = ratings.groupby("movieId").agg(
    average_rating=("rating","mean"),
    rating_count=("rating","count")
).reset_index()

popular_movies = pd.merge(movie_stats, movies, on="movieId")
popular_movies = popular_movies.sort_values(by="average_rating", ascending=False)

print(popular_movies[["title","average_rating","rating_count"]].head(10))

# Task 2: Count movies per genre

# Split genres
genres = movies["genres"].str.split("|")

# Convert list into rows
genres = genres.explode()

# Count each genre
genre_count = genres.value_counts()

print("\nMovies per Genre:")
print(genre_count)

import matplotlib.pyplot as plt

# Plot genre counts
genre_count.plot(kind="bar", figsize=(10,5))

plt.title("Number of Movies per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")

plt.show()

# Task 3: Recommend movies by genre

def recommend_movies(genre):

    # Filter movies that contain the genre
    genre_movies = popular_movies[popular_movies["genres"].str.contains(genre, case=False)]

    # Sort by rating
    recommendations = genre_movies.sort_values(by="rating", ascending=False)

    print("\nTop Movies in", genre, "Genre:\n")
    print(recommendations[["title","rating"]].head(10))


# Example recommendation
recommend_movies("Action")
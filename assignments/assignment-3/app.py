import pandas as pd
import random
import numpy as np
from scipy.stats import pearsonr
from flask import Flask, jsonify, current_app, request

app = Flask(__name__)

# Load ratings data
df = pd.read_csv("ratings.small.csv")

# Create a mapping between data movie IDs and local movie IDs
movie_map = {}
movie_rmap = {}
for i, m in enumerate(sorted(df["movieId"].unique().tolist())):
    movie_map[m] = i
    movie_rmap[i] = m

# Create a dictionary to hold user ratings
user_ratings = {}
num_movies = len(movie_map)
for u in df["userId"].unique():
    user_ratings[u] = np.zeros(num_movies)

# Populate dictionary using data from the data file
for u, m, r in df[["userId", "movieId", "rating"]].values:
    mid = movie_map[m]
    user_ratings[u][mid] = r

# hardcode some data for easy debugging
user_ratings[100957934] = np.zeros(num_movies)
user_ratings[100957934][[0,2,3,4,6,7,8,9,12,45,67,89,120]] = 1

# Load movie ID mapping
df1 = pd.read_csv("movies.csv")
df2 = pd.read_csv("links.csv")
df = df1.merge(df2, on="movieId")
movieId2info = {}
for movieId, title, imdbId in df[["movieId", "title", "imdbId"]].values:
    movieId2info[movieId] = (title, imdbId)


def compute_similarity():
    """A function for computing the similarity between users
    """
    logging.info("Compute similarity")
    users = list(user_ratings.keys())
    sims = {}
    for i, u in enumerate(users):
        for v in users:
            if u == v:
                continue
            corr, _ = pearsonr(user_ratings[u], user_ratings[v])
            sims.setdefault(u, {})[v] = corr
            sims.setdefault(v, {})[u] = corr
    return sims


sims = compute_similarity()


def get_recommendations(user_id, n):
    """A function for generating recommendations
    for a given user.
    """
    logging.info("Generating recommendations...")
    preds = []
    for mid in movie_map.values():
        # get top 20 similar users who have rated this movie
        neighbours = sorted([
                (sim, v) for v, sim in sims[user_id].items()
                if user_ratings[v][mid] > 0
            ], reverse=True)[:20]
        r_mean = np.mean(user_ratings[user_id])

        # Compute the predicted rating of the movie
        total = 0
        sim_total = 0
        for sim, v in neighbours:
            if user_ratings[v][mid] > 0:
                total += sims[user_id][v] * \
                    (user_ratings[v][mid] - np.mean(user_ratings[v]))
                sim_total += sim

        pred = r_mean + (total / sim_total)
        preds.append((pred, mid))

    preds.sort(reverse=True)
    logging.info(preds[:n])
    return preds[:n]


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    chat_id = data["chat_id"]
    if chat_id in user_ratings:
        return jsonify(exists=1)
    else:
        user_ratings[chat_id] = np.zeros(num_movies)
        return jsonify(exists=0)


@app.route("/get_unrated_movie", methods=["POST"])
def get_unrated_movie():
    data = request.get_json()
    chat_id = data["chat_id"]

    # Randomly pick a movie that is not rated by the user
    while True:
        mid = random.randint(0, num_movies-1)
        if user_ratings[chat_id][mid] == 0:
            break

    movie_id = movie_rmap[mid]
    title, imdb_id = movieId2info[movie_id]
    url = "https://www.imdb.com/title/tt{:07d}/".format(imdb_id)

    return jsonify(id=movie_id, title=title, url=url)


@app.route("/rate_movie", methods=["POST"])
def rate_movie():
    data = request.get_json()
    chat_id = data["chat_id"]
    movie_id = data["movie_id"]
    rating = data["rating"]

    mid = movie_map[movie_id]
    user_ratings[chat_id][mid] = rating
    compute_similarity()
    
    return jsonify(status="success")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    chat_id = data["chat_id"]
    top_n = data["top_n"]
    
    if np.sum(np.where(user_ratings[chat_id] > 0, 1, 0)) < 10:
        return jsonify(movies=[])

    recs = get_recommendations(chat_id, top_n)
    data = []
    for _, mid in recs:
        movie_id = movie_rmap[mid]
        title, imdb_id = movieId2info[movie_id]
        url = "https://www.imdb.com/title/tt{:07d}/".format(imdb_id)
        data.append({"title": title, "url": url})
    return jsonify(movies=data)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)

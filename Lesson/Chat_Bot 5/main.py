import logging
import requests
import numpy as np
import pandas as pd
import random
import csv
from flask import Flask, request, jsonify, current_app
from scipy.stats import pearsonr

logging.basicConfig(level=logging.INFO)

# Constant Variables
PORT = 5000
HOST = 'localhost'
API_ENDPOINT = 'localhost:5000'
RATING_PATH = './data/ratings.small.csv'
TITLE_PATH = './data/movies.csv'
LINK_PATH = './data/links.csv'

app = Flask(__name__)


# Create rating matrix, list of users, list of movies
def create_rating_matrix(path):
    df = pd.read_csv(path, sep=',', usecols=['userId', 'movieId', 'rating'])
    df = df.pivot(index='userId', columns='movieId', values='rating')
    df = df.fillna(value=0)
    return  df.values, df.index.values, df.columns.values


# Import the titles
def create_titles(path):
    df = pd.read_csv(path, sep=',', usecols=['movieId', 'title'])
    return df.values


# Import the links
def create_links(path):
    df = pd.read_csv(path, sep=',', usecols=['movieId', 'imdbId'],
                     dtype={'imdbId': str})
    return df.values


# Create rating matrix, users, movies, titles and links
app.rating_matrix, app.users, app.movies = create_rating_matrix(RATING_PATH)
app.titles = create_titles(TITLE_PATH)
app.links = create_links(LINK_PATH)

# Size down the titles to smaller sample set
temp = []
for title in app.titles:
    if title[0] in app.movies.tolist():
        temp.append(title)
app.titles = np.asarray(temp)

# Size down the links to smaller sample set
temp =[]
for link in app.links:
    if link[0] in app.movies.tolist():
        temp.append(link)
app.links = np.asarray(temp)
del temp


# Checks if a User already exists and registers him/her if not
@app.route('/register', methods=['POST'])
def register():
    # Retrieve Data
    data = request.json
    chat_id = data['chat_id']

    # Check if user already exists
    if chat_id in current_app.users.tolist():
        return jsonify({'exists': 1})

    # The chat Id is the new users Id
    current_app.users = np.append(current_app.users, chat_id)

    # Add row of zeros to the rating matrix
    current_app.rating_matrix = np.append(current_app.rating_matrix,
                                          np.zeros((1, current_app.rating_matrix.shape[1])),
                                          axis=0)
    return jsonify({'exists': 0})


# Get a random movie that hasn't been rated by the user yet
@app.route('/get_unrated_movie', methods=['POST'])
def get_unrated_movie():
    data = request.json
    chat_id = data['chat_id']
    # Get the ratings of a user by its userId
    user_ratings = current_app.rating_matrix[np.where(current_app.users == chat_id)]
    print(user_ratings)

    # Get a random movie which is not yet rated
    movie_id = current_app.movies[random.choice(np.where(user_ratings == 0)[1])]
    # Create the Title
    title = current_app.titles[np.where(current_app.titles == movie_id)[0]][0][1]
    # Create URL
    url = 'https://www.imdb.com/title/tt{}/'.format(current_app.links[np.where(current_app.links == movie_id)[0]][0][1])
    return jsonify({
        'id': str(movie_id),
        'title': title,
        'url': url
    })


# Update the ratings matrix after the user has rated it
@app.route('/rate_movie', methods=['POST'])
def rate_movie():
    # Retrieve received data
    data = request.json
    chat_id = data['chat_id']
    movie_id = int(data['movieID'])
    rating = int(data['rating'])

    # Updated rating matrix
    current_app.rating_matrix[np.where(current_app.users == chat_id), np.where(current_app.movies == movie_id)] = rating

    # Write to csv file, so data isn't lost
    row = [str(chat_id), str(movie_id), str(rating), 'N/A']
    with open(RATING_PATH, 'r') as readFile:
        reader = csv.reader(readFile)
        line = list(reader)[-1]
        if line != row:
            with open(RATING_PATH, 'a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow(row)
            writeFile.close()
    readFile.close()
    # Return json string
    return jsonify({'status': 'success'})


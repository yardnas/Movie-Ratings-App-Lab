"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    title, overview, poster_path = (movie['title'], movie['overview'], movie['poster_path'])
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    date = movie['release_date'] #'2020-04-10'
    format = '%Y-%m-%d'
    release_date = datetime.strptime(date, format)

    # TODO: create a movie here and append it to movies_in_db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    new_user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    for num in range(10):
        random_rating = randint(1, 5)
        random_movie = choice(movies_in_db)

        crud.create_rating(new_user, random_movie, random_rating)
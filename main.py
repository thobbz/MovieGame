import random

from flask import Flask, jsonify, render_template, request
from tmdbv3api import Movie, TMDb

app = Flask(__name__)

tmdb = TMDb()
tmdb.api_key = 'f838d2f0dbe942bda16e92644bd7a4a5'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_quote', methods=['GET'])
def get_quote():
    # Select a random movie from the TMDb database
    movie = Movie()
    popular_movies = movie.popular()
    random_movie = random.choice(popular_movies)
    movie_id = random_movie.id

    movie_details = movie.details(movie_id)
    # TODO: Generate an AI-based quote from the selected movie
    quote = "Generated quote here"

    return jsonify(quote=quote, movie_id=movie_id)

@app.route('/check_guess', methods=['POST'])
def check_guess():
    guess = request.json['guess']
    movie_id = request.json['movie_id']
    movie = Movie()
    movie_details = movie.details(movie_id)
    if guess.lower() == movie_details['title'].lower():
        return jsonify(correct=True, message="Congratulations! You guessed the movie correctly.")
    else:
        # TODO: Generate a new AI-based quote from the same movie
        new_quote = "Generated new quote here"
        return jsonify(correct=False, quote=new_quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
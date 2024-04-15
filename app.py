import random

from flask import Flask, jsonify, render_template, request
from tmdbv3api import Movie, TMDb

app = Flask(__name__)

tmdb = TMDb()
tmdb.api_key = 'f838d2f0dbe942bda16e92644bd7a4a5'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    # Select a random movie from the TMDb database
    movie = Movie()
    popular_movies = movie.popular()
    random_movie = random.choice(popular_movies)
    movie_id = random_movie.id

    movie_details = movie.details(movie_id)
    # TODO: Generate an AI-based question about the selected movie
    question = "Generated question here"

    return jsonify(question=question, movie_id=movie_id)

@app.route('/check_guess', methods=['POST'])
def check_guess():
    guess = request.json['guess']
    movie_id = request.json['movie_id']
    movie = Movie()
    movie_details = movie.details(movie_id)
    if guess.lower() == movie_details['title'].lower():
        return jsonify(correct=True, message="Congratulations! You guessed the movie correctly.")
    else:
        # TODO: Generate a new AI-based question about the same movie
        new_question = "Generated new question here"
        return jsonify(correct=False, question=new_question)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
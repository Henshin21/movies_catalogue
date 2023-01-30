from random import random
from flask import Flask, render_template, request
import requests
app = Flask(__name__, static_folder="static", static_url_path="/static")
import tmdb_client

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    available_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']
    if selected_list not in available_lists:
        selected_list = 'popular'
    url = f"https://api.themoviedb.org/3/movie/{selected_list}?api_key=c98f13140ddb6dd3cda199eb01c083cf&language=en-US&page=1"
    response = requests.get(url)
    data = response.json()
    movies = data["results"][:8]
    return render_template("homepage.html", movies=movies, available_lists=available_lists, selected_list=selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   movie_images = tmdb_client.get_movie_images(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)


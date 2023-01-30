import requests

API_TOKEN = "c98f13140ddb6dd3cda199eb01c083cf"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=" + API_TOKEN
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_upcoming_movies():
    endpoint = "https://api.themoviedb.org/3/movie/upcoming?api_key=" + API_TOKEN + "&language=en-US&page=1"
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_top_rated_movies():
    endpoint = "https://api.themoviedb.org/3/movie/top_rated?api_key=" + API_TOKEN + "&language=en-US&page=1"
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_now_playing_movies():
    endpoint = "https://api.themoviedb.org/3/movie/now_playing?api_key=" + API_TOKEN + "&language=en-US&page=1"
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=" + API_TOKEN
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=" + API_TOKEN + "&language=en-US"
    headers = {
        "Authorization": "Bearer " + API_TOKEN
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=" + API_TOKEN
    headers = {}
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key=" + API_TOKEN
    headers = {}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
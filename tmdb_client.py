import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=c98f13140ddb6dd3cda199eb01c083cf"
    api_token = "c98f13140ddb6dd3cda199eb01c083cf"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
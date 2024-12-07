import requests
from celery import shared_task
from .models import Movies
from django.conf import settings  # Import Django settings




@shared_task
def fetch_and_store_movies(start_page=1, end_page=5):
    for page in range(start_page, end_page + 1):
        response = requests.get(
            settings.TMDB_URL,
            params={'api_key': settings.API_KEY, 'language': 'en-US', 'page': page}
        )
        if response.status_code == 200:
            movies = response.json().get('results', [])
            for movie in movies:
                Movies.objects.get_or_create(
                    title=movie['title'],
                    overview=movie['overview'],
                    release_date=movie['release_date'],
                    poster_path=movie['poster_path'],
                    popularity=movie['popularity'],
                    vote_average=movie['vote_average'],
                    vote_count=movie['vote_count']
                )
            return f"Successfully populated {len(movies)} movies from page {page}."
        else:
            return f"Failed to fetch movies: {response.status_code}"

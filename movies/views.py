from rest_framework import viewsets
from movies.models import Movies
from movies.serializers import MoviesSerializer
from django.shortcuts import render

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

# Create your views here.
def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
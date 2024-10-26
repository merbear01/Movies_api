from rest_framework import viewsets
from movies.models import Movies
from movies.serializers import MoviesSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

# Create your views here.

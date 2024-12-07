from movies.models import Movies
import pytest

@pytest.mark.django_db
def test_movies_model():
    # Test movie creation
    movie = Movies.objects.create(
        title='The Shawshank Redemption',
        release_date='1994-09-23',
        popularity=9.3,
        vote_average=8.7,
        vote_count=12345,
    )
    # Validate field values
    assert movie.title == 'The Shawshank Redemption'
    assert str(movie.release_date) == '1994-09-23'
    assert movie.popularity == 9.3
    assert movie.vote_average == 8.7
    assert movie.vote_count == 12345


@pytest.mark.django_db
def test_movies_model_defaults():
    # Test default values
    movie = Movies.objects.create()
    assert movie.title == ''
    assert movie.overview == ''
    assert str(movie.release_date) == '1994-09-23'
    assert movie.poster_path == ''
    assert movie.popularity == 0
    assert movie.vote_average == 0
    assert movie.vote_count == 0


@pytest.mark.django_db
def test_movies_model_str():
    # Test the __str__ method
    movie = Movies.objects.create(title='The Shawshank Redemption')
    assert str(movie) == 'The Shawshank Redemption'
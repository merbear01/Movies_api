# movies/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MoviesViewSet

router = DefaultRouter()
router.register(r'api/movies', MoviesViewSet)  # API paths

urlpatterns = [
    path('api/', include(router.urls)),  # API available under /api/
    path('', views.movie_list, name='movie_list'),  # Homepage
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),  # Movie detail
]

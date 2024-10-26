from django.urls import path, include
from .views import MoviesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'movies', MoviesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
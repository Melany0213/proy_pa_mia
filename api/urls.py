from django.urls import path
from .views import search_movies, movie_detail

urlpatterns = [
    path("movies", search_movies),
    path("movies/<int:movie_id>", movie_detail),
]

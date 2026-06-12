from django.urls import path

from movies import views


app_name="movies"
urlpatterns=[
    path("",views.index,name="home"),
    path("add-movie",views.addMovie,name="add_movie"),
    path("all-movies",views.allMovies,name="all_movies"),
    path("movies/<slug:cat_slug>",views.allMovies,name="movie_filter_category"),
    path("edit-movie/<int:movie_id>",views.editMovie,name="edit_movie"),
    path("movie-detail/<int:movie_id>",views.movieDetail,name="movie_detail"),
    

]
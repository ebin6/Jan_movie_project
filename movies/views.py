from django.shortcuts import render,redirect
from movies.models import Movie
# Create your views here.

def index(request):
    return render(request,"index.html")

def addMovie(request):
    if request.method=="POST":
        movie_name=request.POST["title"]
        desc=request.POST["description"]
        image=request.FILES["poster"]
        date=request.POST["release_date"]
        tr_link=request.POST["trailer_link"]
        movie=Movie(name=movie_name,poster=image,description=desc,trailer_link=tr_link,release_date=date)
        movie.save()
        return redirect("movies:all_movies")
    return render(request,"add-movie.html")

def allMovies(request):
    movies=Movie.objects.all()
    return render(request,"all-movies.html",{"movies":movies})


def editMovie(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"edit-movie.html",{"movie":movie})
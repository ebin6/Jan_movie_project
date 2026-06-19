from django.shortcuts import render,redirect
from movies.models import Movie,Category,ActorMovie,Reviews
from actors.models import Actors
from django.contrib.auth.models import User
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
        cat=request.POST["category"]
        category=Category.objects.get(id=cat)
        movie=Movie(name=movie_name,poster=image,description=desc,trailer_link=tr_link,release_date=date,category=category)
        movie.save()
        return redirect("movies:all_movies")
    return render(request,"add-movie.html")

def allMovies(request,cat_slug=None):
    if cat_slug:
        movies=Movie.objects.filter(category__slug=cat_slug)
    else:
        movies=Movie.objects.all()
    return render(request,"all-movies.html",{"movies":movies})


def editMovie(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    if request.method=="POST":
        movie.name=request.POST["title"]
        movie.description=request.POST["description"]
        movie.poster=request.FILES.get("poster",movie.poster)
        movie.release_date=request.POST["release_date"]
        movie.trailer_link=request.POST["trailer_link"]
        category=request.POST['category']
        cat=Category.objects.get(id=category)
        movie.category=cat
        movie.save()
        return redirect("movies:movie_detail",movie.id)
    return render(request,"edit-movie.html",{"movie":movie,})

def movieDetail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"movie-detail.html",{"movie":movie})

def AddMovieActor(request,movie_id):
    if request.method=="POST":
        movie=Movie.objects.get(id=movie_id)
        actor_id=request.POST["actor"]
        role_name=request.POST['character_name']
        actor=Actors.objects.get(id=actor_id)
        ActorMovie(movie=movie,actor=actor,character_name=role_name).save()
        return redirect("movies:movie_detail",movie_id)

def addReview(request,movie_id):
    if request.method=="POST":
        movie=Movie.objects.get(id=movie_id)
        review=request.POST["comment"]
        rating=request.POST['rating']
        user=User.objects.get(id=request.user.id)
        Reviews(movie=movie,review=review,rating=rating,user=user).save()
        return redirect("movies:movie_detail",movie_id)


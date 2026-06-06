from django.shortcuts import render,redirect
from movies.models import Movie,Category

# Create your views here.

def index(request):
    return render(request,"index.html")

def addMovie(request):
    categories=Category.objects.all()
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
    return render(request,"add-movie.html",{"categories":categories})

def allMovies(request):
    movies=Movie.objects.all()
    return render(request,"all-movies.html",{"movies":movies})


def editMovie(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    categories=Category.objects.all()
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
    return render(request,"edit-movie.html",{"movie":movie,"categories":categories})

def movieDetail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"movie-detail.html",{"movie":movie})


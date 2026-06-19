from django.db import models
from actors.models import Actors
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30,unique=True)
    slug=models.SlugField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name=models.CharField(max_length=50,unique=True)
    poster=models.ImageField(upload_to="posters")
    description=models.TextField()
    trailer_link=models.URLField()
    release_date=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class ActorMovie(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    actor=models.ForeignKey(Actors,on_delete=models.CASCADE)
    character_name=models.CharField(max_length=50)

class Reviews(models.Model):
    review=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

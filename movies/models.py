from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30,unique=True)
    slug=models.SlugField()


class Movie(models.Model):
    name=models.CharField(max_length=50,unique=True)
    poster=models.ImageField(upload_to="posters")
    description=models.TextField()
    trailer_link=models.URLField()
    release_date=models.DateField()
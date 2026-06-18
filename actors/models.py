from django.db import models

# Create your models here.
class Actors(models.Model):
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=30)
    description=models.TextField()
    dob=models.DateField()
    slug=models.SlugField()
    profile_pic=models.ImageField(upload_to="actors",default="actors/default_image.jpg")
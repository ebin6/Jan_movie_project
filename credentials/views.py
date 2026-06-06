from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method=="POST":
        email=request.POST['email']
        f_name=request.POST["f_name"]
        l_name=request.POST["l_name"]
        passwd=request.POST["con_password"]
        if User.objects.filter(username=email).exists():
            return HttpResponse("Username already exists")
        else:
            User.objects.create_user(username=email,first_name=f_name,last_name=l_name,password=passwd).save()
            return redirect("credentials:signin") 

    return render(request,"register.html")

def signin(request):
    if request.method=="POST":
        email=request.POST['email']
        passwd=request.POST["password"]
        user=auth.authenticate(username=email,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect("movies:home")
        else:
            return HttpResponse("Invalid username or password")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("movies:home")
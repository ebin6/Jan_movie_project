from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        email=request.POST['email']
        f_name=request.POST["f_name"]
        l_name=request.POST["l_name"]
        passwd=request.POST["con_password"]
        if User.objects.filter(username=email).exists():
            messages.error(request,"Username already exists")
            return redirect("credentials:signup")
        else:
            User.objects.create_user(username=email,first_name=f_name,last_name=l_name,password=passwd).save()
            messages.success(request,"New account created . Please login to continue")
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
            messages.info(request,"Invalid username or password")
            return redirect("credentials:signin")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("movies:home")
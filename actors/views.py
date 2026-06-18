from django.shortcuts import render
from actors.forms import ActorForm
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from actors.models import Actors
# Create your views here.

'''
def addActor(request):
    if request.method=="POST":
        form=ActorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Added successfully")
    else:
        form=ActorForm()
    return render(request,"add-actor.html",{"my_form":form})
'''

class AddActor(CreateView):
    template_name="add-actor.html"
    model=Actors
    form_class=ActorForm
    success_url="/"

class ListActors(ListView):
    template_name="view-actors.html"
    model=Actors
    context_object_name="actors"

class ActorDetail(DetailView):
    template_name="actor-detail.html"
    model=Actors
    context_object_name="actor"

class EditActor(UpdateView):
    template_name="update-actor.html"
    model=Actors
    form_class=ActorForm
    success_url="/actors/all-actors/"
    
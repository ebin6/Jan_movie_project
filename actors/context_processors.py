from actors.models import Actors
def allActors(request):
    actors=Actors.objects.all()
    return dict(all_actors=actors)
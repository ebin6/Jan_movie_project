from movies.models import Category

def allCategories(request):
    cats=Category.objects.all()
    return {"categories":cats}
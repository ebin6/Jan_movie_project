from django.urls import path

from actors import views
app_name="actors"

urlpatterns=[
    path("add-actor",views.AddActor.as_view(),name="add_actor"),
    path("all-actors/",views.ListActors.as_view(),name="view_actors"),
    path("view-actor/<int:pk>",views.ActorDetail.as_view(),name="actor_detail"),
    path("edit-actor/<int:pk>/",views.EditActor.as_view(),name="edit_actor")
]
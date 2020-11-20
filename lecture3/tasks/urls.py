from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    # single empty route that loads the index function
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]

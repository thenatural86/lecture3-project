from django.urls import path
from . import views

urlpatterns = [
    # single empty route that loads the index function
    path("", views.index, name="index")
]
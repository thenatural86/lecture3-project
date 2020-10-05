from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # pass in request to render function, along with an html template
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

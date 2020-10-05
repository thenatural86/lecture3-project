from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # pass in request to render function, along with a namespaced html template of "hello/index.html"
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, brian!")

def david(request):
    return HttpResponse("Hello, David!")

# pass in 2 args of request and name
def greet(request, name):
    # render request. template AND context that takes the form of a python dictionary of key name and val of name.capitalize
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

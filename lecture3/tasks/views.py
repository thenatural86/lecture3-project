from django import forms

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

# new class to represent form
class NewTaskForm(forms.Form):
    # define all the fields i want the form to have
    task = forms.CharField(label="New Task")
    # client side validation
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    # server side validation
    if request.method == "POST":
        # fills in data from form
        form = NewTaskForm(request.POST)
        # validation function
        if form.is_valid():
           task = form.cleaned_data["task"]
           tasks.append(task)
           return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    # newtaskform passed in as context key/val
    # GET
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
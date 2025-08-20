from django.shortcuts import render

# Create your views here.

# Dummy project list
projects = [
    {"title": "E-Commerce Website", "desc": "Django + React Fullstack app", "link": "#"},
    {"title": "Portfolio Website", "desc": "Personal portfolio in Django", "link": "#"},
    {"title": "Blog App", "desc": "CRUD Blog with Django ORM", "link": "#"},
]

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    return render(request, "portfolio/projects.html", {"projects": projects})

def contact(request):
    return render(request, "portfolio/contact.html")

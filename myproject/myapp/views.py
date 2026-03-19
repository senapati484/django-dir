from django.shortcuts import render
from .forms import BasicForm
from .models import Student, Items

# Home Page with Form
def home(request):
    students = Student.objects.all()
    data = {
        "title": "Welcome to Our Django App 👋",
        "content": "This is the home page of our Django application. Here you can find the latest updates and features.",
        "students": students
    }
    return render(request, "home.html", data)

# About Page
def about(request):
    data = {
        "title": "About Us",
        "content": "This is the about page of our Django application. Here you can find information about our mission, vision, and team."
    }
    return render(request, "about.html", data)

def shoping(request):
    items_list = Items.objects.all()
    data = {
        "title": "Shoping Page",
        "content": "Welcome to our shoping page! Here you can find a variety of products.",
        "items": items_list
    }
    return render(request, "shoping.html", data)

def form(request):
    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
    else:
        form = BasicForm()

    return render(request, "form.html", {"form": form})
from django.shortcuts import render
from .forms import BasicForm

# Home Page with Form
def home(request):
    data = {
        "title": "Welcome to Our Django App 👋",
        "content": "This is the home page of our Django application. Here you can find the latest updates and features.",
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
    data = {
        "title": "Shoping Page",
        "content": "Welcome to our shoping page! Here you can find a variety of products.",
        "items": [
            {
                "name": "Product 1",
                "price": "$10",
                "image": "https://picsum.photos/200?random=1"
            },
            {
                "name": "Product 2",
                "price": "$20",
                "image": "https://picsum.photos/200?random=2"
            },
            {
                "name": "Product 3",
                "price": "$30",
                "image": "https://picsum.photos/200?random=3"
            },
        ]
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
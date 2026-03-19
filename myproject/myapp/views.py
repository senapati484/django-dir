from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

# Home Page
def home(request):
    return render(request, "home.html")

# About Page
def about(request):
    return render(request, "about.html")

# Signup View - Handle both GET (show form) and POST (save to database)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # This saves the user to the database
            user = form.save()
            # Automatically log in the user after signup
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = SignUpForm()
    
    return render(request, 'auth/signup.html', {'form': form})

# Login View - Handle user authentication
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Check if username and password are correct
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Create a session for the user
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard
            else:
                form.add_error(None, 'Invalid username or password!')
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

# Dashboard View - Only accessible to logged-in users
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

# Logout View
def logout(request):
    auth_logout(request)
    return redirect('home')

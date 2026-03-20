from django.shortcuts import redirect, render
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

# Read
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})

@login_required
def dj(request):
    return render(request, 'dj.html')

# Create
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )
    return redirect('home')

# Update
@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.completed = True if request.POST.get('completed') == 'on' else False
        task.save()
        
        return redirect('home')
    return render(request, 'update.html', {'task': task})

# Delete
@login_required
def del_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('home')


    # if request.method == 'POST':
    #     task_id = request.POST.get('task_id')
    #     Task.objects.filter(id=task_id).delete()
    # return redirect('home')

def register_user(request):
    # Registration logic here

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('login_user')

    return render(request, 'register.html')

def login_user(request):
    # Login logic here

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def logout_user(request):
    # Logout logic here
    logout(request)
    return redirect('home')
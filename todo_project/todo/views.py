from django.shortcuts import redirect, render
from .models import Task

# Create your views here.

# Read
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def dj(request):
    return render(request, 'dj.html')

# Create
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
    return redirect('home')

# Update
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.completed = True if request.POST.get('completed') == 'on' else False
        task.save()
        
        return redirect('home')
    return render(request, 'update.html', {'task': task})

# Delete
def del_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')


    # if request.method == 'POST':
    #     task_id = request.POST.get('task_id')
    #     Task.objects.filter(id=task_id).delete()
    # return redirect('home')
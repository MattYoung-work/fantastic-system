from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Todo
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the tasks index.")
    recent_tasks = Todo.objects.order_by('-created_at')[:5]
    context = {
        'recent_tasks': recent_tasks,
    }
    return render(request, 'tasks/index.html', context)

def detail(request, task_id):
    #return HttpResponse(f"You're looking at task {task_id}.")
    task = get_object_or_404(Todo, id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', context)
    #return HttpResponse(f"Task: {task.title}, Description: {task.description}, Created at: {task.created_at}, Completed: {task.completed}")
    #return render(request, 'tasks/detail.html', {'task': task})

def update(request, task_id):
    #return HttpResponse(f"You're updating task {task_id}.")
    task = get_object_or_404(Todo, id=task_id)
    if request.method == 'POST':
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))
    else:
        return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))
    
def new_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Todo(title=title, description=description)
        task.save()
        return HttpResponseRedirect(reverse('tasks:index'))
    else:
        return HttpResponseRedirect(reverse('tasks:index'))
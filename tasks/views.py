from django.shortcuts import render
from django.http import HttpResponse

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
    try:
        task = Todo.objects.get(id=task_id)
    except Todo.DoesNotExist:
        return HttpResponse("Task does not exist.")
    context = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', context)
    #return HttpResponse(f"Task: {task.title}, Description: {task.description}, Created at: {task.created_at}, Completed: {task.completed}")
    #return render(request, 'tasks/detail.html', {'task': task})

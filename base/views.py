from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# Create your views here

def tasklist(request):
    return HttpResponse('To Do list')

class TaskList(ListView):
    model = Task
    context_object_name ='tasks'

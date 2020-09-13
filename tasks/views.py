from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import os

# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by("-id")
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"tasks":  tasks , "form": form}
    return render(request, 'tasks/index.html', context)


def update(request, id):
    task = Task.objects.get(pk=id)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "tasks/update.html", context)


def delete_task(request, id):
    task = Task.objects.get(pk=id)

    if request.method == "POST":
        task.delete()
        return redirect("/")


    context = {"task": task}
    return render(request, "tasks/delete_task.html", context)

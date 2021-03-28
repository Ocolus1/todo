from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import string
from random import choices

def generate_id():
    characters = string.digits + string.ascii_letters
    short_url = "".join(choices(characters, k=6))

    return short_url

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [] 
    
    if request.method == "POST":
        id = generate_id()
        title = request.POST['title']
        completed = request.POST.get('completed', None)
        saved_list = request.session['tasks']
        if completed:
            saved_list.append({"id": id, "title": title, "completed": True})
        else:
            saved_list.append({"id": id, "title": title, "completed": False})
        
        request.session['tasks'] = saved_list

        return redirect("/")

    tasks = request.session["tasks"]
    context = {"tasks":  tasks}
    return render(request, 'tasks/index.html', context)


def update(request, id):
    saved_list = request.session['tasks']
    for i in saved_list:
        if i['id'] == id:
            task = i

    if request.method == "POST":
        new_title = request.POST['title']
        completed = request.POST.get('completed', None)
        saved_list = request.session['tasks']
        for i in saved_list:
            if i['id'] == id:
                i['title'] = new_title
                if completed:
                    i['completed'] = True
                else:
                    i['completed'] = False
            break
        request.session['tasks'] = saved_list
        return redirect("/")

    context = {"task": task}
    return render(request, "tasks/update.html", context)


def delete_task(request, id):
    saved_list = request.session['tasks']
    for i in saved_list:
        if i['id'] == id:
            task = i

    if request.method == "POST":
        saved_list = request.session['tasks']
        for i in saved_list:
            if i['id'] == id:
                saved_list.remove(i)

        request.session['tasks'] = saved_list
        return redirect("/")


    context = {"task": task}
    return render(request, "tasks/delete_task.html", context)

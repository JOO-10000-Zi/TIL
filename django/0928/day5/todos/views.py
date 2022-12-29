from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get("content___")

    Todo.objects.create(content=content)

    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')

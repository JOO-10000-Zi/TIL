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
    # 일할 내용 만들기
    content = request.GET.get("content___")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    # 우선 운쉬 만들기


    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')
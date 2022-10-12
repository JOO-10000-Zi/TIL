from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def index(request):
    users = User.objects.order_by('-pk')
    context = {
        'users':users
    }
    return render(request, 'accounts/accounts.html', context)

def detail(request, pk):
    users = User.objects.get(pk=pk)
    context = {
        'users': users
    }
    return render(request, 'accounts/detail.html', context)
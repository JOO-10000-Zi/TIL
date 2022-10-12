from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
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

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)
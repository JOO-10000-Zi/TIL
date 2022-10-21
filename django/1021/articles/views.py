from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'articles/login.html', context)
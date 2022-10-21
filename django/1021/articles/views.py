
from django.shortcuts import render, redirect
from .models import Article, User
from .forms import ArticleForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
    

@login_required
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article_form = form.save(commit=False)
        article_form.user = request.user
        article_form.save()
        return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    articles = Article.objects.get(pk=pk)

    context = {"article": articles}

    return render(request, "articles/detail.html", context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            form.save()
            return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
            }
        return render(request, 'articles/update.html', context)
    else:
        messages.warning(request, '작성자만 수정 할 수 있어요.')
        return  redirect('articles:detail', article.pk)

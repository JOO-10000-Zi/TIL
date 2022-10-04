import re
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     article_Form = ArticleForm()
#     context = {
#         'article_Form': article_Form,
#     }
#     return render(request, 'articles/new.html', context=context)

def create(request):
    if request.method == 'POST':
        article_Form = ArticleForm(request.POST)
        if article_Form.is_valid():
            article_Form.save()
            return redirect('articles:index')

    else:
        article_Form = ArticleForm()
    context = {
        'article_Form': article_Form,
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)

    else:
        article_form = ArticleForm(instance=article)
    context = {
        'articles_form': article_form
    }
    return render(request, 'articles/update.html', context)
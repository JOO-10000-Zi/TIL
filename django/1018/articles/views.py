from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, '글작성을 완료 했습니다.')
        return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    articles = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=articles)
        if form.is_valid():
            form.save()
            messages.success(request, '글 수정을 완료 했습니다.')
            return redirect('articles:detail', articles.pk)
    else:
        form = ArticleForm(instance=articles)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import article
from django.contrib import messages

# Create your views here.
def index(request):
    articles = article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    form = ArticleForm(request.POST, request.FILES)
    print(request.FILES)
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
    articles = article.objects.get(pk=pk)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    articles = article.objects.get(pk=pk)
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
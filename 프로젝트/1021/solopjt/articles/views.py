from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-pk')
    context={
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    form = ArticlesForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        article.save()
        return redirect('articles:index')
    else:
        form = ArticlesForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    articles = Articles.objects.get(pk=pk)
    context = {
        'articles': articles
    }
    return render(request, 'articles/detail.html', context)
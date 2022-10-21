from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, CommentForm
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
    comment_form = CommentForm()
    comments = articles.comment_set.all()
    context = {
        'articles': articles,
        'comment_form': comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    articles = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticlesForm(request.POST, instance=articles)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', articles.pk)
    else:
        form = ArticlesForm(instance=articles)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)

# 댓글 구현
def comment_create(request, pk):
    article = Articles.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user 
        comment.save()
    return redirect('articles:detail', article.pk )

def comment_delete(request, article_pk, comment_pk):
    comment = CommentForm.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
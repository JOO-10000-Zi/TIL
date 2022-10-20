from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
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
    comment_form = CommentForm()
    comments = articles.comment_set.all()
    context = {
        'articles': articles,
        'comment_form': comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk )

def comment_delete(request, article_pk, comment_pk):
    comment = CommentForm.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reviexs
from .forms import ReviewsForm

# Create your views here.
def index(request):
    reviews = Reviexs.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'articles/index.html', context)
# 직접 접근제어 변경
def create(request):
    if request.user.is_authenticated:
        article_form = ReviewsForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
        else:
            article_form = ReviewsForm()
        context = {
            'article_form':article_form
        }
        return render(request, 'articles/create.html', context)
    else:
        return redirect('accounts:login')

def detail(request, pk):
    reviews = Reviexs.objects.get(pk=pk)

    context = {"reviews": reviews}

    return render(request, "articles/detail.html", context)

# 장고에서 기능을 불러와서 접근제어 구현
@login_required
def update(request, pk):
    reviews = Reviexs.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ReviewsForm(request.POST, instance=reviews)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', reviews.pk)
    else:
        article_form = ReviewsForm(instance=reviews)
    context = {
        'article_form':article_form
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    reviews = Reviexs.objects.get(pk=pk)
    reviews.delete()

    return redirect('articles:index')
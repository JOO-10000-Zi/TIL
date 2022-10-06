from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    review = Movie.objects.order_by('-pk')

    context ={
        'review' : review
    }

    return render(request, "articles/index.html", context)

def create(request):
    return render(request, 'articles/create.html')
    
def addreview(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    runing_time = request.GET.get('runing_time')

    Movie.objects.create(
        title=title,
        content=content,
        runing_time=runing_time,
    )

    return redirect('articles:index')

def detail(request, pk):
    pk = Movie.objects.get(pk=pk)
    context = {
        "pk":pk
    }
    return render(request, 'articles/detail.html', context)

def edit(request):
    pass
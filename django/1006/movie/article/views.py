from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')

    context = {
        'movies': movies
    }
    return render(request, 'article/index.html', context)

# def new(request):
#     movie_form = MovieForm()
#     context = {
#         'movie_form': movie_form
#     }
#     return render(request, 'article/new.html', context)

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('article:index')
    else:
        movie_form = MovieForm()    
    context = {
        'movie_form':movie_form
    }
    return render(request, 'article/new.html', context=context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'article/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('article:detail', movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        'movie_form': movie_form
    }
    return render(request, 'article/update.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('article:index')
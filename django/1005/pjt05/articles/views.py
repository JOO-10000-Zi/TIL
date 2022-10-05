from django.shortcuts import render, redirect
from .models import reviews

# Create your views here.
def index(request):
    review = reviews.objects.order_by('-pk')

    context ={
        'review' : review
    }

    return render(request, "articles/index.html", context)

def create(request):
    return render(request, 'articles/create.html')
    
def addreview(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    created_at = request.GET.get('created_at')
    update_ad = request.GET.get('update_ad')

    reviews.objects.create(
        title=title,
        content=content,
        created_at=created_at,
        update_ad=update_ad,
    )

    return redirect('articles:index')

def detail(request, pk):
    pk = reviews.objects.get(pk=pk)
    context = {
        "pk":pk
    }
    return render(request, 'articles/detail.html', context)

def edit(request):
    pass
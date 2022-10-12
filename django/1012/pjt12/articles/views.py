from symbol import decorators
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewsFrom
from .models import Reviews
# Create your views here.

def index(request):
    reviews = Reviews.objects.order_by("-id")

    context = {
        "Review": reviews,
    }

    return render(request, "articles/index.html", context)


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            reviews_form = ReviewsFrom(request.POST)
            if reviews_form.is_valid():
                reviews_form.save()
                return redirect('articles:index')
        else:
            reviews_form = ReviewsFrom()
        context = {
            'reviews_form':reviews_form
        }
        return render(request, "articles/create.html", context)
    else:
        return redirect('accounts:login')


def detail(request, pk):
    pk = Reviews.objects.get(id=pk)

    context = {"id": pk}

    return render(request, "articles/detail.html", context)


def delete(request, pk):
    pk = Reviews.objects.get(id=pk)
    pk.delete()

    return redirect("articles:index")


def edit(request, pk):
    # reviews = Reviews.objects.get(id=pk)
    # if request.method == "POST":
    #     reviews_form = ReviewsFrom(request.POST, instance=reviews)
    #     if reviews_form.is_valid():
    #         reviews_form.save()
    #         return redirect('articles:detail')
    # else:
    #     reviews_form = ReviewsFrom()
    # context = {
    #     'reviews_form':reviews_form
    # }
    # return render(request, 'articles/edit.html', context)
    pk = Reviews.objects.get(id=pk)

    context = {"pk": pk}

    return render(request, "articles/edit.html", context)

@login_required
def update(request, pk):
    reviews = Reviews.objects.get(id=pk)
    if request.method == "POST":
        reviews_form = ReviewsFrom(request.POST, instance=reviews)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('articles:detail')
    else:
        reviews_form = ReviewsFrom()
    context = {
        'reviews_form':reviews_form
    }
    return render(request, 'articles/edit.html', context)


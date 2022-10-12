from django.shortcuts import render, redirect
from .models import Reviews
# Create your views here.

def index(request):
    reviews = Reviews.objects.order_by("-id")

    context = {
        "Review": reviews,
    }

    return render(request, "articles/index.html", context)


def create(request):

    return render(request, "articles/create.html")


def send(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    update_at = request.GET.get("update_at")

    Reviews.objects.create(
        title=title,
        content=content,
        created_at=created_at,
        update_at=update_at,
    )

    return redirect("articles:index")


def detail(request, pk):
    pk = Reviews.objects.get(id=pk)

    context = {"id": pk}

    return render(request, "articles/detail.html", context)


def delete(request, pk):
    pk = Reviews.objects.get(id=pk)
    pk.delete()

    return redirect("articles:index")


def edit(request, pk):
    pk = Reviews.objects.get(id=pk)

    context = {"pk": pk}

    return render(request, "articles/edit.html", context)


def update(request, pk):
    pk = Reviews.objects.get(id=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    pk.title = title
    pk.content = content

    pk.save()

    return redirect("articles:detail", pk.pk)


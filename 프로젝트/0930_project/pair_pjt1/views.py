from datetime import date
from django.shortcuts import render, redirect
from .models import Review
from django.db.models import Q

# Create your views here.
def index(request):
    reviews = Review.objects.all().order_by("id")

    context = {
        "Review": reviews,
    }

    return render(request, "index.html", context)


def create(request):

    return render(request, "create.html")


def send(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    update_ad = request.GET.get("update_ad")

    Review.objects.create(
        title=title,
        content=content,
        created_at=created_at,
        update_ad=update_ad,
    )

    return redirect("pair:index")


def detail(request, pk):
    pk = Review.objects.get(id=pk)

    context = {"id": pk}

    return render(request, "detail.html", context)


def delete(request, pk):
    pk = Review.objects.get(id=pk)
    pk.delete()

    return redirect("pair:index")


def edit(request, pk):
    pk = Review.objects.get(id=pk)

    context = {"pk": pk}

    return render(request, "edit.html", context)


def update(request, pk):
    pk = Review.objects.get(id=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    pk.title = title
    pk.content = content

    pk.save()

    return redirect("pair:detail", pk.pk)


def search(request):
    content_list = Review.objects.all()  # 모든 데이데터베이스
    search = request.GET.get(
        "search", ""
    )  # search에 검색쿼리 정보 저장 검색창했을때 리퀘스트정보에서 서치정보가 없디면 "" 빈공간을 반환
    if (
        search
    ):  # seacrch가 True라면 서치리스트는 모든 데이터베이스 안에서 필터를 통해 걸른다 (타이틀에 search 변수의 인자가 있다면 반환)
        search_list = content_list.filter(Q(title__icontains=search))  #
    context = {
        "searched": search_list,
        "search": search,
    }  # 컨텍스트 변수에 딕트로 묶어서 전송

    return render(request, "search.html", context)

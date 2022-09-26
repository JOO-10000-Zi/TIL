from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    name = request.GET.get("ball")
    context = {
        "name": name,
    }
    return render(request, "pong.html", context)


def holzzak(request, num):
    if num == 0:
        check = f"{num}은 0 입니다."
    elif num % 2 == 1:
        check = f"{num}은 홀수입니다."
    elif num % 2 == 0:
        check = f"{num}은 짝수입니다."
    context = {"num": check}

    return render(request, "holzzak.html", context)


def sachik(request, num1, num2):
    add = num1 + num2
    bbegi = num1 - num2
    gob = num1 * num2
    nanoogi = num1 // num2

    context = {
        "num1": num1,
        "num2": num2,
        "add": add,
        "bbegi": bbegi,
        "gob": gob,
        "nanoogi": nanoogi,
    }
    return render(request, "sachik.html", context)


def past(request):
    return render(request, "past.html")


def boogi(request):
    in_name = request.GET.get("pa")
    users = ["두바이거지", "아랍왕자", "인디언", "뉴욕거지", "스파이더맨", "돌", "이번생이 첨이네요"]
    imgs = [
        "https://www.seohakant.com/data/editor/2105/d090d356085b8bc710258f2ba0419275_1621904026_9196.jpg",
        "https://img.ridicdn.net/cover/2057182420/xxlarge#1",
        "https://nimage.newsway.co.kr/photo/2019/05/27/20190527000035_0640.jpg",
        "https://image.news1.kr/system/photos/2013/6/14/497343/article.jpg/dims/optimize",
        "https://www.sisajournal.com/news/photo/first/201707/img_170343_1.png",
        "https://thumbs.dreamstime.com/b/stones-balance-colourfull-stons-outdoor-106896340.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR30_ufhWyPQhwJLwRFd_sTK4iE4_2rZr90rGdlFr73w2PuGmUUeGnLDGkpRHpKCdwQD6w&usqp=CAU",
    ]
    you = random.choice(range(len(users)))
    human = users[you]
    img = imgs[you]
    context = {
        "name": in_name,
        "text": human,
        "img": img,
    }

    return render(request, "boogi.html", context)

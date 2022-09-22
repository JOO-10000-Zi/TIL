from django.shortcuts import render
import random
# Create your views here.
def index(request):
    names = ['주세환','김아연','주지현']
    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    context = {
        'name' : name,
        'greetings' : [
            '안녕~', 'Hello', '메롱~'
        ],
        'imades' : [
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
        ]
    }
    return render(request, 'welcome.html', context)

def today_dinner(request):
    menus = ['집밥', '컵라면', '펀의점', '김밥', '돈까스', '피자', '!!!!굶어!!!!!']
    menu = random.choice(range(len(menus)))
    imgs = [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVC1XPW452waVPnhColkMuk1VsSKgDekQQSQ&usqp=CAU',
        'https://contents.lotteon.com/itemimage/_v031651/LM/88/01/12/85/03/21/1_/00/1/LM8801128503211_001_1.jpg/dims/resizef/720X720',
        'https://www.fetv.co.kr/data/photos/20211040/art_16335725352249_db4489.jpg',
        'https://recipe1.ezmember.co.kr/cache/recipe/2016/06/29/e7401296033ab8e4297cd53d71e1bba91.jpg',
        'http://www.dailygrid.net/news/photo/202010/385865_281543_333.jpg',
        'https://w.namu.la/s/8c2aebf04d4c6e0ae24ebf3b3789cb064f353da40f0a2916630ee33cc34742414ac8427b8765569e84d615a24cac7bc389ada2e5c60579541ea8b41be9b22db66f14a3db5f981a2cc93bba229a752932915474cffbb7d3fe3cc41022e163a2b2b720c118309e131b9dbe8fdfda5c449b',
        'https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/201710/19/seouleconomy/20171019155334747fgof.png'
    ]
    gangcoo = menus[menu]
    img = imgs[menu]
    context = {
        'name' : gangcoo,
        'img' : img,

    }
    return render(request, 'today_dinner.html', context)

def lotto(request):
    return render(request, 'lotto.html')    
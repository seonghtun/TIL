from django.shortcuts import render
from .models import Burger
# Create your views here.

def main(request):
    return render(request, "burgers/main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    # Template 전달 dict 객체
    context = {
        "burgers" : burgers,
    }
    return render(request, "burgers/burger_list.html", context)

def burger_search(request):
    # print(request.GET)
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    
    else :
        burgers = Burger.objects.none()
    context = {
        "burgers" : burgers
    }
    print(burgers)

    return render(request, "burgers/burger_search.html",context)
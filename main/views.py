from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import requests


#Requests


def home(request):
    return render(request, 'home.html')

def about(request):
    data = requests.get(f'https://dummyjson.com/products/').json()
    return render(request, 'about.html', {"data":data})

def cards(request):
    data = requests.get('https://dummyjson.com/products').json()
    return render(request, 'cards.html', {'data':data['products']})

def detail(request, id):
    data = requests.get(f'https://dummyjson.com/products/{id}').json()
    return render(request, 'detail.html', {"data": data})

def confirmation(request):
    return render(request, 'confirmation.html')

def base(request):
    return render(request, 'base.html')

def bought(request):
    return render(request, 'bought.html')

# Create your views here.


# def home_views1(request):
#     return render(request, "home.html")
    

# def about_views1(request):
#     return render(request, "about.html")


# def cards_views1(request):
#     return render(request, "cards.html")


# def home_views(request: HttpResponse):
#     return HttpResponse("Assalomu alaykum <h1>Django</h1><br><hr><br><a href='/about'>about</a>")


# def about_views(request: HttpResponse):
#     now = datetime.now()
#     return HttpResponse(f"<h2>About Page</h2><a href='/'>Home</a><br><hr><br><h3>{now}</h3>")

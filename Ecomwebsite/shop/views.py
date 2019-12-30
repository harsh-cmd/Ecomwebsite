from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math
# Create your views here.


def index(request):
    # product = Product.objects.all()
    # n = len(product)
    # nslides = n//4 + math.ceil((n/4) - (n//4))
    # #context = {'product':product, "nslides":nslides , "range":range(1,nslides)}

    allProdu = []
    catprods = Product.objects.values('category')
    cat = {item['category'] for item in catprods}
    for cats in cat:
        a = Product.objects.filter(category=cats)
        n=len(a)
        nslides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProdu.append([a, range(1, nslides), nslides])
    context = {'allProdu':allProdu}
    return render(request, 'shop/index.html',context)


def contact(request):
    return HttpResponse('contact')


def about(request):
    return render(request, 'shop/about.html')


def tracker(request):
    return HttpResponse('tracker')


def search(request):
    return HttpResponse('search')


def productview(request):
    return HttpResponse('')


def checkout(request):
    return HttpResponse('ABout')


def contact(request):
    return HttpResponse('ABout')


def contact(request):
    return HttpResponse('ABout')
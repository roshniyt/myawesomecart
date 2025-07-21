from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))

    # allProds = [
    #     [products, range(1, nSlides), nSlides],
    #     [products, range(1, nSlides), nSlides]
    # ]
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds} #set comprehension to get unique categories 
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides+1), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("This is tracker page")

def search(request):
    return HttpResponse("This is search page")

def productview(request):
    return HttpResponse("This is productview page")

def checkout(request):
    return HttpResponse("This is checkout page")

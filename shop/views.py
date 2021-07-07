from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
# from shop.models import Product


def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allprods = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allprods': allprods}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productview(request, myid):
    # fetch the product using the id
    product = Product.objects.filter(id=myid)
    # print(product)
    return render(request, "shop/prodview.html", {'product': product[0]})


def Checkout(request):
    return render(request, "shop/checkout.html")

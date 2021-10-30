from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


def home (request, category_slug=None):
    category_page=None
    products=None
    if category_slug !=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category_page, available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request, 'shop/home.html', {'products':products,'category':category_page})

def product (request):
    return render(request, 'shop/product.html')

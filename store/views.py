from django.shortcuts import render, get_object_or_404
from .models import Product
from greatkart1.models import Category

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug) #porzadkowanie produktow do kategorii
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    return render(request, 'store/store.html', {'products': products, 'product_count': product_count,})

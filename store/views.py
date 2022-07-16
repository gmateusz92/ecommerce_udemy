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

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #store - models category a nastepnie pobieramy slug z  getkard1 slug, ctaegory__slug daje dostep do slugu tego modelu
    except Exception as e:
        raise e
    return render(request, 'store/product_detail.html', {'single_product': single_product})
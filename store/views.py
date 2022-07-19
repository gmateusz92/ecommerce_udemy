from django.shortcuts import render, get_object_or_404
from .models import Product
from greatkart1.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug) #porzadkowanie produktow do kategorii
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)  # 6 produktow chcemy widziec na stronie
        page = request.GET.get('page')  # http://127.0.0.1:8000/store/?page=2 dlatego 'page'
        paged_products = paginator.get_page(page)  # 6 produktow jest tu przechowywanych i one sa wysylane do template
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id') #mam lacznie np 8 produktow
        paginator = Paginator(products, 3) # 6 produktow chcemy widziec na stronie
        page = request.GET.get('page') # http://127.0.0.1:8000/store/?page=2 dlatego 'page'
        paged_products = paginator.get_page(page) # 6 produktow jest tu przechowywanych i one sa wysylane do template
        product_count = products.count()
    return render(request, 'store/store.html', {'products': paged_products, 'product_count': product_count,})

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #store - models category a nastepnie pobieramy slug z  getkard1 slug, ctaegory__slug daje dostep do slugu tego modelu
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e
    return render(request, 'store/product_detail.html', {'single_product': single_product, 'in_cart': in_cart})

def search(request):
    return HttpResponse('search page')
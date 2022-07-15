from django.urls import path
from . import views

#app_name = 'website' #jezeli dodajemy tutaj app_name to w templates dajemy np href="{% url 'website:contact' %}

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'), # 127.0.0.1:800/store/category_slug/product_slug


]
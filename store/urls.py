from django.urls import path
from . import views

#app_name = 'website' #jezeli dodajemy tutaj app_name to w templates dajemy np href="{% url 'website:contact' %}

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), #trzeba dodac category/ bo jest slug i koljeny path bez tego nie zadziala
    path('search/', views.search, name='search')
]
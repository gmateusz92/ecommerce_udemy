from django.urls import path
from . import views

app_name = 'website' #jezeli dodajemy tutaj app_name to w templates dajemy np href="{% url 'website:contact' %}

urlpatterns = [
    path('', views.home, name='home'),

]
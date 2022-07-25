from django.db import models
from greatkart1.models import Category
from django.shortcuts import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)# jezeli skasujemy Category to wszystkie produkty z dnaje kategorii zostana usnunieta
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self): #fukcja uzyta w template navbar
            return reverse('product_detail', args =[self.category.slug, self.slug ]) # product detail to name w urls

    def __str__(self):
        return self.product_name

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model): #wybieranie rozmiaru/koloru produktu
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # jezeli produkt zostanie usuniety to variations tez
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product
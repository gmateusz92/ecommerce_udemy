from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self): #fukcja uzyta w template navbar
            return reverse('products_by_category', args =[self.slug]) # product category to name w urls

    def __str__(self):
        return self.category_name
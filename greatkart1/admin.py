from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin): # pokazuje w naglowkach category name i slug w Categories w admin panel
    prepopulated_fields = {'slug':('category_name',)} #slug automatycznie wypelnia drugie pole tym co wpisalem w category name
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from .models import Product
from .models import Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin): # z models
    list_display = ('product', 'variation_category', 'variation_value', 'is_active') #wyswietla w panelu administratora w liscie
    list_editable = ('is_active',) # zeby mozna bylo edytowac w panelu admina
    list_filter = ('product', 'variation_category', 'variation_value') #panel do flitrowania z prawej strony

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)


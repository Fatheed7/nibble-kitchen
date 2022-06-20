from django.contrib import admin
from .models import Category, Ingredients, Product, Sub_Categories 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image_url')
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name')

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name')

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name','is_allergen','has_sub_ingredient')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Categories, SubCategoriesAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Product, ProductAdmin)


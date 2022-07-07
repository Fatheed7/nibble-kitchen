from django.contrib import admin
from .models import Category, Ingredients, Product, Sub_Categories, Rating
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'in_stock', 'price', 'on_sale', 'sale_price', 'image_url')
    search_fields = ('name',)
    ordering = ('sku',)
    list_filter = ('category',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'ingredients':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name')

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','name')

class IngredientsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('friendly_name','name','is_allergen','has_sub_ingredient')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('product','title','content','rating','date_posted','author')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Categories, SubCategoriesAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)


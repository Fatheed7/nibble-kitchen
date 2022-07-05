from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg    
from sortedm2m.fields import SortedManyToManyField

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Sub_Categories(models.Model):

    class Meta:
        verbose_name_plural = "Sub-Categories"
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Ingredients(models.Model):

    class Meta:
        verbose_name_plural = "Ingredients"
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    is_allergen = models.BooleanField(default=False, null=True, blank=True)
    has_sub_ingredient = models.BooleanField(default=False, null=True, blank=True)
    sub_ingredients = models.ManyToManyField('self', blank=True)
    sub_category = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    medium_sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large_sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ingredients = SortedManyToManyField('Ingredients', db_column='friendly_name', blank=True)

    def __str__(self):
        return self.name

class Comments(models.Model):

    class Meta:
        verbose_name_plural = "Comments"

    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.author.username + ', ' + self.title[:40]
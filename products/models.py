from django.db import models

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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    ingredients = models.ManyToManyField('Ingredients', db_column='friendly_name', blank=True)

    def __str__(self):
        return self.name
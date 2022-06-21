from django import forms
from .models import Ingredients, Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        ingredients = Ingredients.objects.all()
        friendly_names_ingredients = [(i.id, i.get_friendly_name()) for i in ingredients]

        self.fields['category'].choices = friendly_names
        self.fields['ingredients'].choices = friendly_names_ingredients
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
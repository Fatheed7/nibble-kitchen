from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .widgets import CustomClearableFileInput
from .models import Ingredients, Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all(), widget=FilteredSelectMultiple("Ingredients", False))

    class Media:
        js = ('/admin/jsi18n/',)


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
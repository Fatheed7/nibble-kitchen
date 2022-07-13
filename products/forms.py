from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.safestring import mark_safe
from .widgets import CustomClearableFileInput
from .models import Ingredients, Product, Category, Rating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=FilteredSelectMultiple("Ingredients", False))
    sale_price = forms.DecimalField(max_digits=6, decimal_places=2,
                                    required=True)
    has_sizes = forms.BooleanField(label='Has Sizes', required=True)
    in_stock = forms.BooleanField(label='In Stock', required=True)

    class Media:
        js = ('/admin/jsi18n/',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        ingredients = Ingredients.objects.all()
        friendly_names_ingredients = [(
            i.id, i.get_friendly_name()) for i in ingredients]

        self.fields['category'].choices = friendly_names
        self.fields['ingredients'].choices = friendly_names_ingredients
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'title', 'content']

    rating = forms.ChoiceField(choices=[
        (0.5, mark_safe('<span class="visually-hidden">Rating 0.5</span>')),
        (1, mark_safe('<span class="visually-hidden">Rating 1.0</span>')),
        (1.5, mark_safe('<span class="visually-hidden">Rating 1.5</span>')),
        (2, mark_safe('<span class="visually-hidden">Rating 2.0</span>')),
        (2.5, mark_safe('<span class="visually-hidden">Rating 2.5</span>')),
        (3, mark_safe('<span class="visually-hidden">Rating 3.0</span>')),
        (3.5, mark_safe('<span class="visually-hidden">Rating 3.5</span>')),
        (4, mark_safe('<span class="visually-hidden">Rating 4.0</span>')),
        (4.5, mark_safe('<span class="visually-hidden">Rating 4.5</span>')),
        (5, mark_safe('<span class="visually-hidden">Rating 5.0</span>'))],
        widget=forms.RadioSelect(),)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Please enter the title of your review',
            'content': 'What did you like or dislike?',
            'rating': 'Please enter your rating'
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

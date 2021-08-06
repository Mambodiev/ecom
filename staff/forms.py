from django import forms

from cart.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title_en',
            'slug_en',
            'featured',
            # 'description',
            'price',
            'available_colours',
            'available_sizes',
            'primary_category',
            'secondary_categories',
            'title_fr',
            'slug_fr',
        ]

from django.forms import ModelForm

from product.models import Product


class ProductForm(ModelForm):
    """Product form for adding details to the site"""
    class Meta:
        model = Product
        fields = '__all__'
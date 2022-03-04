from django.forms import ModelForm

from product.models import Product

"""
   Product form collection
"""
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

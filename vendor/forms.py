from django import forms
from django.forms import ModelForm

from product.models import Product


class ProductForm(ModelForm):
    """Product form for adding details to the site"""
    class Meta:
        """Model is for the Product"""
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'})
        }
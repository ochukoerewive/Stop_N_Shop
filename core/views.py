from django.shortcuts import render

from product.models import Product

# Create your views here.
def index(request):
    """ creating view page for newest product"""
    newest_products = Product.objects.all()[0:8]
    
    return render(request, 'index.html', {'newest_products': newest_products})

def contact(request):
    """ creating view page for contact us"""
    return render(request, 'contact.html')
    
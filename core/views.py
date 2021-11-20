from django.shortcuts import render

from product.models import Product

# Create your views here.
def index(request):
    newest_products = Product.objects.all()[0:8]
    
    return render(request, 'index.html', {'newest_products': newest_products})

def contact(request):
    return render(request, 'contact.html')
    
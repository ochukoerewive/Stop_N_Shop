from django.db import models

from product.models import Product
from vendor.models import Vendor

# Create your models here.
class Order(models.Model):
    """ Information required for order placed """
    #order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    zipcode = models.CharField(max_length=20, null=False, blank=False)
    place = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    vendors = models.ManyToManyField(Vendor, related_name='orders')

    class Meta:
        """ Adding and substracting order to be placed """
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    """ knowing the quantity and the price for Item bought"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
    
    def get_total_price(self):
        return self.price * self.quantity
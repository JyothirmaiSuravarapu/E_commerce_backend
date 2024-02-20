from django.db import models
from django.conf import settings
from Shop.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="cart", null=True)#for testing purpose
    item = models.ForeignKey(Product, on_delete=models.CASCADE )
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} * {self.item}'
    
    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, 'o.2f')
        return float_total
    
class Order(models.Model):
    order_items = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=300, blank=True, null=True)
    order_id = models.CharField(max_length=200, blank=True, null=True)

    #To get the total amt to pay
    def get_totals(self):
        total = 0
        for x in self.order_items.all():
            total+=float(x.get_total())
            return total

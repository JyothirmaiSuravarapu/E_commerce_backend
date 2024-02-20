from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    main_img = models.ImageField(upload_to='Product')
    Product_name = models.CharField(max_length=254)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='Category') ## Category deletd then all the associated products also deleted
    Preview_text = models.TextField(max_length=300, verbose_name='Preview Text')
    details = models.TextField(max_length=1500, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_name
    
    class Meta:
        ordering = ['-created',] ## display the order details in descreing order

    






from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField(default=10) 
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/images/default.jpg'

    def __str__(self):
        return self.name


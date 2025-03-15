from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='categories'

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.TextField(blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return f'{self.first_name}{self.second_name}'
    
class Product(models.Model):
    name=models.CharField(max_length=20)
    categories=models.ManyToManyField(Category) 
    price=models.DecimalField(max_digits=7,decimal_places=1)
    original_price=models.DecimalField(max_digits=7,decimal_places=1)
    description=models.CharField(max_length=100)
    detail_description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/',blank=True)
    is_sale=models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
    def discount_percentage(self):
        if self.original_price > 0:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return f'{discount:.2f}%'
        return '0%'
    

class Slider(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=7,decimal_places=1)
    original_price=models.DecimalField(max_digits=7,decimal_places=1)
    description=models.CharField(max_length=100)
    detail_description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.name



class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    date=models.DateTimeField(default=datetime.datetime.now)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.product
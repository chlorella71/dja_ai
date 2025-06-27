from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.BigIntegerField()
    category = models.CharField(max_length=100)
    inStock = models.BooleanField(default=True)

    class Meta:
        db_table="products"

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        db_table="users"

    def __str__(self):
        return self.name

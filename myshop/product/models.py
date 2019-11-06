import os

from django.db import models
from myshop.settings import STATIC_URL


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=10, default="USD")
    desctiption = models.CharField(max_length=100)
    type_product = models.CharField(max_length=100)
    photo = models.ImageField(upload_to= "product", blank=True)

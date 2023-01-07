from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=160)
    discount = models.IntegerField(default=0, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')

  
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=160)
    discount = models.IntegerField(blank=True)


from django.db import models

from datetime import datetime

# Create your models here.
class Recipes(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created = models.DateField()

class Products(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=40)
    created = models.DateField()

class Ingredients(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    weight_type = models.CharField(max_length=20)
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_sku = models.CharField(max_length=100)
    product_description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.product_name}, {self.product_sku}'

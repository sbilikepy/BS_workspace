from django.db import models
from typing import List


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # id = models.IntegerField

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    products: List[Product] = models.ManyToManyField(
        Product,
        related_name="orders",
        through="OrderItem"
    )
    # owner: User = models.CharField(max_length=255)
    # id = models.IntegerField()
    def __str__(self):
        products_str = ", ".join([str(product) for product in self.products.all()])
        return f"Order {self.pk}: {products_str}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"order#{self.order}: {self.product}, amount -> {self.amount}"

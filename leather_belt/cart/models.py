from catalog.models import Product


from django.contrib.auth.models import User
from django.db import models


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_product = models.CharField(max_length=5, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class Order(models.Model):
    status = models.CharField(max_length=50, default='Создан')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    size_product = models.CharField(max_length=5, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)




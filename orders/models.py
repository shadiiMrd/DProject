from django.db import models
from accounts.models import User
from main.models import *


class Order(models.Model):
    ORDER_STATUS = (
        ('ثبت شده' , 'ثبت شده'),
        ('در حال تهیه', 'در حال تهیه'),
        ('تهیه شده', 'تهیه شده'),
        ('تحویل داده شد', 'تحویل داده شد'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    table = models.PositiveIntegerField()
    status = models.CharField(choices=ORDER_STATUS, max_length=20 , default=ORDER_STATUS[0][0])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def total_items(self):
        return sum(item.count for item in self.order_items.all())

    @property
    def total_price(self):
        return sum(item.count * item.menu.price for item in self.order_items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.count} x {self.menu.name}"

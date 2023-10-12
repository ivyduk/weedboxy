from django.db import models
from config.mixins import ModelMixin, PricingMixin
from polymorphic.models import PolymorphicModel


# Create your models here.

class OrderItem(ModelMixin, PricingMixin, PolymorphicModel):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    

    def get_cost(self):
        return self.price * self.quantity



class Order(ModelMixin, PricingMixin):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, related_name="order_items", blank=True, null=True
        )


    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            ]
 
    def __str__(self):
        return f'Order {self.first_name}'

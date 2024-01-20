import random
import string
from django.db import models
from config.mixins import ModelMixin, PricingMixin
from polymorphic.models import PolymorphicModel
from apps.users.models import UserAccount


# Create your models here.

class SKUItem(ModelMixin, PricingMixin, PolymorphicModel):
    sku_code = models.CharField(max_length=200, unique=True, editable = False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity_in_stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.sku_code
    
    def generate_random_sku_code(self, length=20):
        # Valid Characters for SKU (alphanumeric)
        characters = string.ascii_letters + string.digits
        
        # Generrate random SKU code of specific length
        sku_code = 'WB'.join(random.choice(characters) for _ in range(length))
    
        return sku_code
    
    def save(self, *args, **kwargs):
        self.sku_code = self.generate_random_sku_code()
        super(SKUItem, self).save(*args, **kwargs)


class Order(ModelMixin):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    user = models.ForeignKey(
        UserAccount, 
        related_name='orders', 
        on_delete=models.CASCADE, 
        null=True
    )


    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            ]
 
    def __str__(self):
        return f'Order {self.first_name}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(ModelMixin):

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    order = models.ForeignKey(
        Order, 
        related_name='items', 
        on_delete=models.CASCADE
    )
    
    sku_item = models.ForeignKey(
        SKUItem,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    
    def get_cost(self):
        return self.price * self.quantity

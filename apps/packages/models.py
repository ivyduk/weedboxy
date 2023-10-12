from django.db import models
from apps.orders.models import OrderItem


class PackageItem(OrderItem):
    description = models.TextField()

    def __str__(self):
        return self.name


class Package(OrderItem):
    description = models.TextField()
    is_active = models.BooleanField()
    package_items = models.ManyToManyField(PackageItem, related_name='package_items', blank=True)

    def __str__(self):
        return self.name
    


    
    
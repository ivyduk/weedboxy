from django.db import models
from apps.orders.models import SKUItem


class PackageItem(SKUItem):

    def __str__(self):
        return self.name


class Package(SKUItem):
    is_active = models.BooleanField()
    package_items = models.ManyToManyField(PackageItem, related_name='package_items', blank=True)

    def __str__(self):
        return self.name
    


    
    
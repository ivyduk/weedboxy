from django.db import models
from config.mixins import ModelMixin
from apps.packages.models import PackageItem

class Service(PackageItem):
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):

        return self.name


class ServiceFeature(ModelMixin):
    name=models.CharField(max_length=100)
    description = models.TextField(default="")
    service=models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ServicesContact(ModelMixin):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True,  )
    services = models.ForeignKey(Service, on_delete=models.CASCADE )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
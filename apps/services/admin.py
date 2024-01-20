from django.contrib import admin

# Register your models here.

from .models import ServicesContact
from .models import Service
from .models import ServiceFeature

admin.site.register(ServicesContact)
admin.site.register(Service)
admin.site.register(ServiceFeature)
from django.urls import path
from apps.services.views import services_home


urlpatterns = [
    path('', services_home,  name='services_home'),
]


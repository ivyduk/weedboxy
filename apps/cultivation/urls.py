from django.urls import path
from apps.cultivation.views import cultivation_home


urlpatterns = [
    path('', cultivation_home,  name='cultivation_home'),
]

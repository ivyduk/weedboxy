from django.urls import path
from . import views
from apps.users import views as users_views


urlpatterns = [  
    
    path('', views.index, name='index'),
    path('about/', views.about_home, name='about_home'),
    path('subscribe/', users_views.subscribe_home, name='subscribe_home'), 
]

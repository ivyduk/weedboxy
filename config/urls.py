"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps.services import urls as service_urls
from apps.users import urls as users_urls
from apps.courses import urls as course_urls
from apps.products import urls as product_urls
from apps.cultivation import urls as cultivation_urls
from apps.orders import urls as order_urls
from django.conf import settings
from django.conf.urls.static import static
import config.views as config_views
from apps.courses.views import CourseListView


urlpatterns = [
    path('users/', include(users_urls)),
    path('services/', include(service_urls)),
    path('courses/', include(course_urls)),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('products/', include(product_urls)),
    path('cultivation/', include(cultivation_urls)),
    path('orders/', include(order_urls)),
    path('cart/', config_views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/', config_views.add_to_cart, name='add_item'),
    path('remove_item_quantity_from_cart/<int:item_id>/', config_views.remove_item_quantity_from_cart, name='remove_item_quantity'),
    path('remove_item_from_cart/<int:item_id>/', config_views.remove_item_from_cart, name='remove_item'),
    

     
]

# TODO: Adjust before to release to production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import  path
from apps.products.views import products_home
from . import views


urlpatterns = [
    path('', products_home, name='products_home'),
    path('categories/<int:category_id>/', views.ProductListView.as_view(), name='product_list_filtered'),

]

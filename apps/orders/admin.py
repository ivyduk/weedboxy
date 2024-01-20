from django.contrib import admin

# Register your models here.

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['sku_item']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 
                    'city', 'paid']
    list_filter = ['paid']
    inlines = [OrderItemInline]
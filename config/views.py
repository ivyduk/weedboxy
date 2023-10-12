from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from config.cart import Cart
from apps.products.models import Product
from apps.cultivation.models import CultivationPlan



def cart(request):

    return render(request, "cart.html", )


def add_to_cart(request, item_id):
    cart = Cart(request)
    cart.add(item_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_item_quantity_from_cart(request, item_id):
    cart = Cart(request)
    cart.remove_item_quantity(item_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),)

def remove_item_from_cart(request, item_id):
    cart = Cart(request)
    cart.remove_item(item_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), )
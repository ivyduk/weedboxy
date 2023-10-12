from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(item, cart):
    keys = cart.cart.keys()
    for id in keys:
        if int (id) == item.id:
            return True
    return False


@register.filter (name='cart_quantity')
def cart_quantity(item, cart):
    keys = cart.cart.keys()
    for id in keys:
        if int (id) == item.id:
            return str(cart.cart.get(id).get('quantity'))
    return str(0)
from decimal import Decimal
from django.conf import settings
from apps.orders.models import OrderItem


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.cupon_id = self.session.get('cupon_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
          
    def add(self, item_id, quantity=1, update_quantity=False):
        item = OrderItem.objects.get(id=item_id)
        item_id = str(item_id)

        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price)
            }
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

        return True
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove_item_quantity(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart:
            if self.cart[item_id]['quantity'] == 1:
                del self.cart[item_id]
            else:
                self.cart[item_id]['quantity'] -= 1
            self.save()

    def remove_item(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart:
            del self.cart[item_id]
        self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = OrderItem.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def is_in_cart(self, item_id):
        return item_id in self.cart

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def get_item_quantity(self, item_id):
        return self.cart[item_id]['quantity']

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    @property
    def cart_count(self):
        count = self.__len__() if self.cart.values() else 0
        return str(count)

    
from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from config.cart import Cart
from .models import Order
from django.contrib.auth.decorators import login_required



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            cart_items = list(cart)
            cart_total = cart.get_total_price()

            for item in cart:
                print(item)
                OrderItem.objects.create(
                    order=order,
                    sku_item=item['item'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order, 'cart_items':cart_items, 'cart_total': cart_total })
    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


    


def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user) 
    return render(request, 'orders/order_history.html', {'orders': orders})



def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_cost = sum(item.get_cost() for item in order.items.all())

    return render(request, 'orders/order_detail.html', {'order': order, 'total_cost': total_cost})


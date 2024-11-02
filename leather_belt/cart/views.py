from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from catalog.forms import ProductForm
from .forms import CartItemForm, OrderForm
from .models import CartItem, OrderItem
from catalog.models import Product


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'myapp/index.html', {'products': products})

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    data = {
        'title': 'Корзина',
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart/cart.html', data)

@login_required
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        selected_size =request.POST['selected_size']

        cart_item, created = CartItem.objects.get_or_create(product=product,
                                                    user=request.user, size_product=selected_size)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def order_view(request):
    cart = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         price=item.product.price,
                                         quantity=item.quantity,
                                         size_product=item.size_product,
                                         user=item.user,
                                         total_price=item.product.price * item.quantity)

                # OrderItem.total_price = item.product.price * item.quantity
                order.save()

            CartItem.objects.filter(user=request.user).delete()

            return redirect('cart:order_confirmation')

            # title = 'Заказ успешно создан'

            # return render(request, 'cart/order_confirmation.html', {'order': order, 'title': title})
    else:
        form = OrderForm()

    return render(request, 'cart/order.html', {'form': form})


def order_confirmation_view(request):
    orders = OrderItem.objects.filter(user=request.user)
    for i in orders:
        last_order = i.order.id
    data = {
        'title': 'Заказ успешно создан',
        'order': last_order,
    }
    return render(request, 'cart/order_confirmation.html', data)

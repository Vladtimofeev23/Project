from django.forms import ModelForm

from cart.models import CartItem, Order


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'size_product', 'quantity', 'user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['cart_items', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Email",
            "address": "Адрес",
            "postal_code": "Почтовый индекс",
            "city": "Город",
        }
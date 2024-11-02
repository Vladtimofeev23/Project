from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from cart.models import Order, OrderItem
from .forms import LoginUserForm, RegisterUserForm


@login_required
def profile(request):
    myorders = OrderItem.objects.filter(user=request.user)
    u = []
    for i in myorders:
        u += [i.order.id]
    myset = list(set(u))
    orders = Order.objects.all()
    data = {
        'title': 'Личный кабинет',
        'user': request.user,
        'myorders': myorders,
        'u': myset,
    }
    return render(request, 'users_login/personal_area.html', data)


# def user_view(request, user_id):
#     user = User.objects.get(id=user_id)
#     data = {
#         'title': 'Личный кабинет',
#         'user': user,
#     }
#     return render(request, 'users_login/personal_area.html', data)


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'users_login/login.html'
    extra_context = {
        'title': 'Авторизация'
    }


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'users_login/register.html'
    success_url = reverse_lazy('users_login:login')

    extra_context = {
        'title': 'Регистрация'
    }

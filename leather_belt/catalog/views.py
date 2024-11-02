from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Product


def catalog(request):
    belts = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'belts': belts, 'title': 'Каталог'})


def catalog_mens_belts(request):
    belts = Product.objects.all().filter(category='1')
    return render(request, 'catalog/catalog_mens_belts.html', {'belts': belts, 'title': 'Мужские ремни'})


def catalog_womens_belts(request):
    belts = Product.objects.all().filter(category='2')
    return render(request, 'catalog/catalog_womens_belts.html', {'belts': belts, 'title': 'Женские ремни'})


class AddProduct(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/add_product.html'
    fields = ['category', 'name', 'color', 'size', 'slug', 'image', 'characteristics', 'description', 'price']
    success_url = reverse_lazy('/catalog/')
    permission_required = 'users_login.add_product'

    extra_context = {
        'title': 'Добавление продукта'
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/details_view_product.html'
    context_object_name = 'product'

    extra_context = {
        'title': model.name,
    }


class SearchProduct(ListView):
    template_name = 'catalog/list_belts.html'
    context_object_name = 'list_belts'
    extra_context = {
        'title': 'Результаты поиска',
    }

    def get_queryset(self):
        return Product.objects.filter(Q(name__contains=self.request.GET.get('q')))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['q'] = self.request.GET.get('q')
    #     return context
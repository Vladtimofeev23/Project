from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('mens_belts/', views.catalog_mens_belts, name='mens_belts'),
    path('womens_belts/', views.catalog_womens_belts, name='womens_belts'),
    path('search/', views.SearchProduct.as_view(), name='search'),

]
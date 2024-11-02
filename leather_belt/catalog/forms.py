from .models import Product
from django.forms import ModelForm, TextInput, Select


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'name', 'color', 'size', 'slug', 'image', 'characteristics', 'description', 'price']

        # widgets = {
        #     'category': Select(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Выберите категорию',
        #     }),
        #     'name': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Наименование',
        #     }),
        #     'color': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Цвет',
        #     }),
        #     'size': TextInput(attrs={
        #         'placeholder': 'Размер',
        #     })
        # }


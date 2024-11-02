from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории, к которым относятся товары"""
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])


# SIZE_CHOICES = (
#     ('100', '100'),
#     ('105', '105'),
#     ('110', '110'),
#     ('115', '115'),
#     ('120', '120'),
#     ('125', '125'),
#     ('130', '130'),
# )

SIZE_CHOICES = {
    "100": "100",
    "105": "105",
    "110": "110",
    "115": "115",
    "120": "120",
    "125": "125",
    "130": "130"
}


class Product(models.Model):
    """Модель описания продукта"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию'
                                 )
    name = models.CharField(max_length=200, verbose_name='Наименование')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    size = models.JSONField(default=SIZE_CHOICES, verbose_name='Размер')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='static/catalog/img', blank=True, verbose_name='Фото')
    characteristics = models.TextField(blank=True, verbose_name='Характеристики')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('catalog:product_detail', args=[self.id, self.slug])



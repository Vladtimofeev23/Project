# Generated by Django 4.2.13 on 2024-07-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/catalog/img', verbose_name='Фото'),
        ),
    ]

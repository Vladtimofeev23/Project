# Generated by Django 4.2.13 on 2024-07-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitem_options_cartitem_size_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size_product',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
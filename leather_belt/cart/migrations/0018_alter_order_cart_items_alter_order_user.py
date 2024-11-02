# Generated by Django 4.2.13 on 2024-07-20 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0017_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cart.cartitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
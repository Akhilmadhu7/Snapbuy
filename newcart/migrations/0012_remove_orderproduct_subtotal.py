# Generated by Django 4.0.6 on 2022-07-23 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newcart', '0011_remove_order_subtotal_orderproduct_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='subtotal',
        ),
    ]

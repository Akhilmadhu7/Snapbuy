# Generated by Django 4.0.6 on 2022-07-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0010_rename_product_lap_cartproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='subtotal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

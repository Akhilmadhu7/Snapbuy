# Generated by Django 4.0.6 on 2022-08-09 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_adminside', '0012_product_diccount_price_alter_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='diccount_price',
            new_name='discount_price',
        ),
    ]

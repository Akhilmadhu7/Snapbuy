# Generated by Django 4.0.6 on 2022-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_adminside', '0007_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=20),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newcart', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.CharField(default=100, max_length=200),
        ),
    ]

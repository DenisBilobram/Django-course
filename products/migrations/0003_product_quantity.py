# Generated by Django 3.1.4 on 2020-12-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]

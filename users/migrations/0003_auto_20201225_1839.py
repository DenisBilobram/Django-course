# Generated by Django 3.1.4 on 2020-12-25 10:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201225_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 10, 39, 20, 725677, tzinfo=utc)),
        ),
    ]

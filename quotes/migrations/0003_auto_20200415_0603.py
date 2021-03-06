# Generated by Django 3.0.3 on 2020-04-15 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20200305_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='stock',
            name='location',
            field=models.TextField(default='default'),
        ),
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]

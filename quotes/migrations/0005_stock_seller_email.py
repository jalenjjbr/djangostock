# Generated by Django 3.0.3 on 2020-04-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_auto_20200415_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='seller_email',
            field=models.EmailField(default='default@default.com', max_length=254),
        ),
    ]

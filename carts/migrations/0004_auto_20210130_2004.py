# Generated by Django 3.1.5 on 2021-01-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20210130_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

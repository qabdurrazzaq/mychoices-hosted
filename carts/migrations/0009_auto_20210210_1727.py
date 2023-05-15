# Generated by Django 3.1.5 on 2021-02-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210209_1731'),
        ('carts', '0008_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='products.Variation'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopingCart', '0002_auto_20191107_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopingcart',
            name='json_products_id',
        ),
        migrations.AddField(
            model_name='shopingcart',
            name='json_product_ids',
            field=models.CharField(default="{'buyed_product_ids': []}", max_length=500),
        ),
    ]

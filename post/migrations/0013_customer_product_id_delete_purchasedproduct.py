# Generated by Django 5.0.1 on 2024-01-25 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_purchasedproduct_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PurchasedProduct',
        ),
    ]

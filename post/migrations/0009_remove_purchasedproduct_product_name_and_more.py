# Generated by Django 5.0.1 on 2024-01-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_remove_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='product_name',
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='product',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

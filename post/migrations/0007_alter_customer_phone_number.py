# Generated by Django 5.0.1 on 2024-01-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_customer_purchasedproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

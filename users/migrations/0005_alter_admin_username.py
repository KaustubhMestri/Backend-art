# Generated by Django 5.0 on 2024-05-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_addtocart_admin_bookorders_product_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=254),
        ),
    ]

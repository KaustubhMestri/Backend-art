# Generated by Django 5.0 on 2024-05-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_addtocart_delete_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookorders',
            name='productimage',
        ),
        migrations.RemoveField(
            model_name='bookorders',
            name='totalprice',
        ),
        migrations.RemoveField(
            model_name='bookorders',
            name='useruid',
        ),
    ]
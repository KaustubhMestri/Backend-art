# Generated by Django 5.0 on 2024-05-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('userid', models.CharField(max_length=100)),
                ('prodid', models.CharField(max_length=100)),
            ],
        ),
    ]

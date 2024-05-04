# Generated by Django 5.0.4 on 2024-05-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useruid', models.CharField(default='0000', max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('productimage', models.ImageField(default='abc.jpg', upload_to='')),
                ('productid', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useruid', models.CharField(default='0000', max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('useremail', models.EmailField(max_length=254)),
                ('userphone', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('taluka', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('sellerid', models.CharField(max_length=255)),
                ('sellername', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.CharField(max_length=255)),
                ('productimage', models.ImageField(default='abc.jpg', upload_to='')),
                ('productid', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('deliverycharge', models.IntegerField(default=0)),
                ('totalprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selleremail', models.EmailField(max_length=254)),
                ('productname', models.CharField(max_length=255)),
                ('productdescription', models.TextField()),
                ('productprice', models.IntegerField()),
                ('deliverycharge', models.IntegerField()),
                ('productImg1', models.ImageField(upload_to='')),
                ('productImg2', models.ImageField(upload_to='')),
                ('productImg3', models.ImageField(upload_to='')),
                ('productImg4', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useruid', models.CharField(default='0000', max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('productimage', models.ImageField(default='abc.jpg', upload_to='')),
                ('productid', models.CharField(max_length=255)),
            ],
        ),
    ]

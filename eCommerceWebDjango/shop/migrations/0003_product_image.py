# Generated by Django 4.1.4 on 2023-02-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='No Image', upload_to='shops/images'),
        ),
    ]

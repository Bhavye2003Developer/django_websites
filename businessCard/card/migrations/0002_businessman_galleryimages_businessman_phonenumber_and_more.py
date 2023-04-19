# Generated by Django 4.1.7 on 2023-04-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessman',
            name='galleryImages',
            field=models.ImageField(default='No image', upload_to=''),
        ),
        migrations.AddField(
            model_name='businessman',
            name='phoneNumber',
            field=models.CharField(default='+919999999999', help_text='Enter phone number with country code', max_length=50),
        ),
        migrations.AddField(
            model_name='businessman',
            name='userImage',
            field=models.ImageField(default='No image', upload_to=''),
        ),
        migrations.AddField(
            model_name='businessman',
            name='worksByUser',
            field=models.TextField(default='Enter a list of works by user', max_length=1000),
        ),
    ]

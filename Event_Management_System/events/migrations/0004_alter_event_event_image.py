# Generated by Django 4.2.3 on 2023-07-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_event_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
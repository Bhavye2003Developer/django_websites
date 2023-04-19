# Generated by Django 4.1.7 on 2023-03-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
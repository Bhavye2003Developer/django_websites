# Generated by Django 4.1.4 on 2023-03-05 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_comments_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='postTitle',
        ),
    ]

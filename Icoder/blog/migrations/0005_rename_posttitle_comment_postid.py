# Generated by Django 4.1.4 on 2023-03-05 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_post_comment_posttitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postTitle',
            new_name='postID',
        ),
    ]

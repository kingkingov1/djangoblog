# Generated by Django 4.2.11 on 2024-06-08 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_postinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='postinfo',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated',
        ),
    ]

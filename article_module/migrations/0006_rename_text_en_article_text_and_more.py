# Generated by Django 4.2.3 on 2023-11-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0005_alter_article_options_remove_article_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text_en',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='text_fa',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_fa',
        ),
    ]

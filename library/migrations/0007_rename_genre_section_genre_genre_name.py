# Generated by Django 4.1.7 on 2023-03-22 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_genre_remove_book_genre_book_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_section',
            new_name='genre_name',
        ),
    ]
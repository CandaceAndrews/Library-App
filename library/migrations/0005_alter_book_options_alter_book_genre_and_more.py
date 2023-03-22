# Generated by Django 4.1.7 on 2023-03-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_book_date_published_book_year_published_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('education', 'Education'), ('graphic novel', 'Graphic Novel'), ('horror', 'Horror'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('thriller', 'Thriller'), ('mystery', 'Mystery'), ("children's literature", "Children's Literature"), ('biography', 'Biograpy'), ('adventure', 'Adventure'), ('cookbook', 'Cookbook'), ('historical', 'Historical'), ('fiction', 'Fiction'), ('nonfiction', 'Non-fiction'), ('science fiction', 'Science Fiction')], max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
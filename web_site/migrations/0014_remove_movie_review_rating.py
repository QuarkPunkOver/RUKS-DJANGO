# Generated by Django 4.0.1 on 2022-02-23 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0013_movie_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='review_rating',
        ),
    ]

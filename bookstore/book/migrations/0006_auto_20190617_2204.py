# Generated by Django 2.2.1 on 2019-06-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publicationDate',
            field=models.DateField(),
        ),
    ]

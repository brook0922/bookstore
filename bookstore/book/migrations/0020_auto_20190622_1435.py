# Generated by Django 2.2.1 on 2019-06-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20190622_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]

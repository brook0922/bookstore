# Generated by Django 2.2.1 on 2019-06-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20190617_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='titleNo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('author', models.CharField(max_length=128, unique=True)),
                ('publisher', models.CharField(max_length=128, unique=True)),
                ('publicationDate', models.DateField()),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['-publicationDate'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(unique=True, verbose_name=range(1, 5))),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='country',
            field=models.CharField(max_length=30),
        ),
    ]

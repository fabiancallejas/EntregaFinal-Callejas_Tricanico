# Generated by Django 4.0.4 on 2022-06-12 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_disco_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disco',
            old_name='tracklist',
            new_name='content',
        ),
    ]

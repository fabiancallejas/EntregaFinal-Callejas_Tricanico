# Generated by Django 4.0.4 on 2022-06-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0011_alter_post_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categorias',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesPost/'),
        ),
    ]

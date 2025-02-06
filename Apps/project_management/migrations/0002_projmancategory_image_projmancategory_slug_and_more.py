# Generated by Django 4.2.11 on 2025-02-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projmancategory',
            name='image',
            field=models.ImageField(default=1, upload_to='proj/category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projmancategory',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projmancoworking',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projmanproject',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]

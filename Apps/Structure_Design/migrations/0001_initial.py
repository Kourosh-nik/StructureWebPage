# Generated by Django 5.1.6 on 2025-02-09 18:25

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STRCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='str/category')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRGravitySys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRLateralSys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRPanelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='bim/banner')),
                ('image_title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('mini_title1', models.CharField(max_length=1000)),
                ('mini_title2', models.CharField(max_length=1000)),
                ('mini_title3', models.CharField(max_length=1000)),
                ('mini_description1', models.TextField()),
                ('mini_description2', models.TextField()),
                ('mini_description3', models.TextField()),
                ('slider1_description', models.TextField()),
                ('slider2_description', models.TextField()),
                ('slider3_description', models.TextField()),
                ('project_base_title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='STRTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='training_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRCoworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('illustration', models.TextField(blank=True, null=True)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('coworker_opinion', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/coworking')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Structure_Design.strcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRCoworkingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coworking_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Structure_Design.strcoworking')),
            ],
        ),
        migrations.CreateModel(
            name='STRProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('illustration', models.TextField(blank=True, null=True)),
                ('characteristic', models.TextField(blank=True, null=True)),
                ('employer_opinion', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/project')),
                ('total_Area', models.FloatField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Structure_Design.strcategory')),
                ('gravity_loading_sys', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Structure_Design.strgravitysys')),
                ('lateral_loading_sys', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Structure_Design.strlateralsys')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='STRProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Structure_Design.strproject')),
            ],
        ),
    ]

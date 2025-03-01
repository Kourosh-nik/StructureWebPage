# Generated by Django 5.1.6 on 2025-02-14 13:44

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
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='bim/video')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='bim/pdf')),
                ('image', models.ImageField(upload_to='image/coworking')),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('land_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usage', models.CharField(max_length=255)),
                ('num_floors', models.PositiveIntegerField()),
                ('num_basement_floors', models.PositiveIntegerField()),
                ('gravity_load_system', models.CharField(max_length=255)),
                ('lateral_load_system', models.CharField(max_length=255)),
                ('project_location', models.CharField(max_length=255)),
                ('construction_year', models.PositiveIntegerField()),
                ('parking_capacity', models.PositiveIntegerField()),
                ('building_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('building_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('floor_height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longest_span', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material_type', models.CharField(choices=[('Concrete', 'بتنی'), ('Steel', 'فلزی'), ('Composite', 'مختلط')], max_length=100)),
                ('foundation_type', models.CharField(max_length=255)),
                ('seismic_design_category', models.CharField(max_length=100)),
                ('wind_load', models.DecimalField(decimal_places=2, max_digits=5)),
                ('snow_load', models.DecimalField(decimal_places=2, max_digits=5)),
                ('design_code', models.CharField(max_length=255)),
                ('analysis_software', models.CharField(max_length=255)),
                ('design_software', models.CharField(max_length=255)),
                ('structural_drawings', models.FileField(blank=True, null=True, upload_to='structural_design/drawings/')),
                ('calculation_report', models.FileField(blank=True, null=True, upload_to='structural_design/reports/')),
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
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='bim/video')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='bim/pdf')),
                ('image', models.ImageField(upload_to='image/project')),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('land_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usage', models.CharField(max_length=255)),
                ('num_floors', models.PositiveIntegerField()),
                ('num_basement_floors', models.PositiveIntegerField()),
                ('gravity_load_system', models.CharField(max_length=255)),
                ('lateral_load_system', models.CharField(max_length=255)),
                ('project_location', models.CharField(max_length=255)),
                ('construction_year', models.PositiveIntegerField()),
                ('parking_capacity', models.PositiveIntegerField()),
                ('building_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('building_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('floor_height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longest_span', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material_type', models.CharField(choices=[('Concrete', 'بتنی'), ('Steel', 'فلزی'), ('Composite', 'مختلط')], max_length=100)),
                ('foundation_type', models.CharField(max_length=255)),
                ('seismic_design_category', models.CharField(max_length=100)),
                ('wind_load', models.DecimalField(decimal_places=2, max_digits=5)),
                ('snow_load', models.DecimalField(decimal_places=2, max_digits=5)),
                ('design_code', models.CharField(max_length=255)),
                ('analysis_software', models.CharField(max_length=255)),
                ('design_software', models.CharField(max_length=255)),
                ('structural_drawings', models.FileField(blank=True, null=True, upload_to='structural_design/drawings/')),
                ('calculation_report', models.FileField(blank=True, null=True, upload_to='structural_design/reports/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Structure_Design.strcategory')),
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

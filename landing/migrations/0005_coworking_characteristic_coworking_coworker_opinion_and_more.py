# Generated by Django 4.2.11 on 2024-11-26 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_project_characteristic_project_employer_opinion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coworking',
            name='characteristic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coworking',
            name='coworker_opinion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coworking',
            name='illustration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coworking',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CoworkingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coworking_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='landing.coworking')),
            ],
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BIM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bimtraining',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

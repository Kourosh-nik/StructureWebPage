# Generated by Django 4.2.11 on 2025-02-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BIM', '0002_bimcategory_slug_alter_bimcoworking_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bimcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-10 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Structure_Design', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strcoworking',
            name='content',
        ),
        migrations.RemoveField(
            model_name='strproject',
            name='content',
        ),
    ]

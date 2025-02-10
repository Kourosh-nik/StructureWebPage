# Generated by Django 5.1.6 on 2025-02-10 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Retrofit', '0002_remove_retrocoworking_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='retrocoworking',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retrocoworking',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='retrocoworking',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='retrocoworking',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='bim/pdf'),
        ),
        migrations.AddField(
            model_name='retrocoworking',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='bim/video'),
        ),
        migrations.AddField(
            model_name='retroproject',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retroproject',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='retroproject',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='retroproject',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='bim/pdf'),
        ),
        migrations.AddField(
            model_name='retroproject',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='bim/video'),
        ),
    ]

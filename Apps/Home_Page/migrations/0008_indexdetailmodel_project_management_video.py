# Generated by Django 5.1.6 on 2025-02-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0007_indexdetailmodel_benefit_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexdetailmodel',
            name='project_management_video',
            field=models.FileField(default=1, upload_to='site_detail/video'),
            preserve_default=False,
        ),
    ]

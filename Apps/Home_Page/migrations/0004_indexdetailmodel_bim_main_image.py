# Generated by Django 5.1.6 on 2025-02-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0003_rename_about_us_description_aboutusdetailmodel_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexdetailmodel',
            name='bim_main_image',
            field=models.ImageField(default=1, upload_to='site_detail/image'),
            preserve_default=False,
        ),
    ]

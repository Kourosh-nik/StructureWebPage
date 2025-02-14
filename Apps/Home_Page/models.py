from django.db import models
from django_jalali.db import models as jmodels
from Apps.BIM.models import BIMProject


class SiteDetailModel(models.Model):
    title = models.CharField(max_length=10000)
    logo = models.ImageField(upload_to='site_detail/image')
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    footer_text = models.TextField()
    contact_us_text = models.TextField()
    telegram_id = models.CharField(max_length=250)   # Enter Telegram id or robot id without @
    enamad_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    enamad_url = models.URLField(null=True, blank=True)
    kasbokar_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    kasbokar_url = models.URLField(null=True, blank=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)


class IndexDetailModel(models.Model):
    title = models.CharField(max_length=10000)
    banners_title = models.CharField(max_length=10000)
    banners_text = models.TextField()
    banner_image1 = models.ImageField(upload_to='site_detail/image')
    banner_image2 = models.ImageField(upload_to='site_detail/image')
    banner_image3 = models.ImageField(upload_to='site_detail/image')
    banner_image4 = models.ImageField(upload_to='site_detail/image')
    bim_banner_image = models.ImageField(upload_to='site_detail/image')
    benefit_banner_image = models.ImageField(upload_to='site_detail/image')
    bim_top_project = models.ForeignKey(BIMProject, on_delete=models.SET_NULL, null=True, blank=True)
    bim_top_project_image = models.ImageField(upload_to='site_detail/image')
    bim_top_project_description = models.TextField()
    project_management_banner_image = models.ImageField(upload_to='site_detail/image')
    retrofit_image = models.ImageField(upload_to='site_detail/image')
    software_image = models.ImageField(upload_to='site_detail/image')
    structure_design_image = models.ImageField(upload_to='site_detail/image')
    project_management_video = models.FileField(upload_to='site_detail/video')
    management_4d_image1 = models.ImageField(upload_to='site_detail/image')
    management_4d_image2 = models.ImageField(upload_to='site_detail/image')
    management_4d_image3 = models.ImageField(upload_to='site_detail/image')
    management_4d_image4 = models.ImageField(upload_to='site_detail/image')



class AboutUsDetailModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    manager_fullname = models.CharField(max_length=100)
    manager_position = models.TextField()
    banner1 = models.ImageField(upload_to='about/image')
    banner2 = models.ImageField(upload_to='about/image')


class ContactUsModel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


# This model is designed for the user to download the sample file,
# fill it out, and upload it to the dashboard.
class SampleFileModel(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='sample/file')

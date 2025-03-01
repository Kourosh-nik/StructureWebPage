from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class SoftPanelModel(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='bim/banner')
    image_title = models.CharField(max_length=1000)
    description = models.TextField()
    mini_title1 = models.CharField(max_length=1000)
    mini_title2 = models.CharField(max_length=1000)
    mini_title3 = models.CharField(max_length=1000)
    mini_description1 = models.TextField()
    mini_description2 = models.TextField()
    mini_description3 = models.TextField()
    slider1_description = models.TextField()
    slider2_description = models.TextField()
    slider3_description = models.TextField()
    project_base_title = models.CharField(max_length=1000)


class BaseModel(models.Model):
    deleted = models.BooleanField(default=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

# Create your models here.
class SoftCategory(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='soft/category')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Software:category', args=[self.slug])


class SoftProject(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='bim/video', null=True, blank=True)
    pdf = models.FileField(upload_to='bim/pdf', null=True, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(SoftCategory, on_delete=models.SET_NULL, null=True, blank=True)
    version = models.CharField(max_length=50)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    supported_platforms = models.CharField(max_length=255)  # ex: Windows, macOS, Linux
    license_type = models.CharField(max_length=100, choices=[('Free', 'رایگان'), ('Paid', 'پرداختی'), ('Subscription', 'اشتراکی')])
    features = models.TextField()  # ویژگی‌های نرم‌افزار
    official_website = models.URLField()
    download_file = models.FileField(upload_to='soft/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Software:project_detail', args=[self.slug])


class SoftProjectImage(models.Model):
    project = models.ForeignKey(SoftProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"


class SoftTraining(BaseModel):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='training_images/')
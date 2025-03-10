from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class RetroPanelModel(models.Model):
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
class RetroCategory(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='retro/category')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Retrofit:category', args=[self.slug])


class RetroProject(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='bim/video', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # عرض جغرافیایی (lat)
    longitude = models.FloatField(null=True, blank=True)  # طول جغرافیایی (lon)
    pdf = models.FileField(upload_to='bim/pdf', null=True, blank=True)
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(RetroCategory, on_delete=models.SET_NULL, null=True, blank=True)
    building_age = models.PositiveIntegerField()  # عمر ساختمان (سال)
    current_seismic_resistance = models.CharField(max_length=255)  # مقاومت لرزه‌ای فعلی
    retrofit_strategy = models.TextField()  # استراتژی بهسازی (مثال: ژاکت بتنی، بادبندها، مقاوم‌سازی پی)
    retrofitting_materials = models.TextField()  # مواد مورد استفاده
    expected_performance_level = models.CharField(max_length=255)  # سطح عملکرد پس از بهسازی
    estimated_cost = models.PositiveIntegerField()  # هزینه برآوردی
    retrofit_design_file = models.FileField(upload_to='retrofitting/designs/', null=True,
                                            blank=True)  # فایل طراحی مقاوم‌سازی

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Retrofit:project_detail', args=[self.slug])

    def get_file_name(self):
        return self.retrofit_design_file.name.split('/')[-1]


class RetroProjectImage(models.Model):
    project = models.ForeignKey(RetroProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class RetroCoworking(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='bim/video', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # عرض جغرافیایی (lat)
    longitude = models.FloatField(null=True, blank=True)  # طول جغرافیایی (lon)
    pdf = models.FileField(upload_to='bim/pdf', null=True, blank=True)
    image = models.ImageField(upload_to='image/coworking')
    category = models.ForeignKey(RetroCategory, on_delete=models.SET_NULL, null=True, blank=True)
    building_age = models.PositiveIntegerField()  # عمر ساختمان (سال)
    current_seismic_resistance = models.CharField(max_length=255)  # مقاومت لرزه‌ای فعلی
    retrofit_strategy = models.TextField()  # استراتژی بهسازی (مثال: ژاکت بتنی، بادبندها، مقاوم‌سازی پی)
    retrofitting_materials = models.TextField()  # مواد مورد استفاده
    expected_performance_level = models.CharField(max_length=255)  # سطح عملکرد پس از بهسازی
    estimated_cost = models.PositiveIntegerField()  # هزینه برآوردی
    retrofit_design_file = models.FileField(upload_to='retrofitting/designs/', null=True,
                                            blank=True)  # فایل طراحی مقاوم‌سازی

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Retrofit:coworking_detail", args=[self.slug])

    def get_file_name(self):
        return self.retrofit_design_file.name.split('/')[-1]


class RetroCoworkingImage(models.Model):
    coworking = models.ForeignKey(RetroCoworking, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coworking_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.coworking.title}"


class RetroTraining(BaseModel):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='training_images/')
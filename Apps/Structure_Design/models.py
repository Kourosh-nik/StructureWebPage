from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class STRPanelModel(models.Model):
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
class STRCategory(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='str/category')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Structure_Design:category', args=[self.slug])



class STRProject(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='bim/video', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # عرض جغرافیایی (lat)
    longitude = models.FloatField(null=True, blank=True)  # طول جغرافیایی (lon)
    pdf = models.FileField(upload_to='bim/pdf', null=True, blank=True)
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(STRCategory, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)  # زیربنا (مترمربع)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)  # مساحت زمین (مترمربع)
    usage = models.CharField(max_length=255)  # کاربری (مسکونی، تجاری، اداری و ...)
    num_floors = models.PositiveIntegerField()  # تعداد طبقات
    num_basement_floors = models.PositiveIntegerField()  # تعداد طبقات زیرزمین
    gravity_load_system = models.CharField(max_length=255)  # سیستم باربر ثقلی (مثال: دال بتنی، تیر و ستون فلزی)
    lateral_load_system = models.CharField(max_length=255)  # سیستم باربر جانبی (مثال: قاب خمشی، دیوار برشی)
    project_location = models.CharField(max_length=255)  # مکان پروژه
    construction_year = models.PositiveIntegerField()  # سال ساخت
    parking_capacity = models.PositiveIntegerField()  # تعداد پارکینگ تأمین‌شده
    building_length = models.DecimalField(max_digits=10, decimal_places=2)  # طول ساختمان (متر)
    building_width = models.DecimalField(max_digits=10, decimal_places=2)  # عرض ساختمان (متر)
    floor_height = models.DecimalField(max_digits=5, decimal_places=2)  # ارتفاع طبقات (متر)
    longest_span = models.DecimalField(max_digits=10, decimal_places=2)  # طول بلندترین دهانه (متر)

    material_type = models.CharField(max_length=100, choices=[('Concrete', 'بتنی'), ('Steel', 'فلزی'),
                                                              ('Composite', 'مختلط')])  # نوع مصالح
    foundation_type = models.CharField(max_length=255)  # نوع فونداسیون (مثال: رادیه، نواری، منفرد)
    seismic_design_category = models.CharField(max_length=100)  # دسته‌بندی طراحی لرزه‌ای
    wind_load = models.DecimalField(max_digits=5, decimal_places=2)  # بار باد (kn/m2)
    snow_load = models.DecimalField(max_digits=5, decimal_places=2)  # بار برف (kn/m2)

    design_code = models.CharField(max_length=255)  # آیین‌نامه طراحی (مثال: مبحث ۶، AISC, ASCE 7)
    analysis_software = models.CharField(max_length=255)  # نرم‌افزار تحلیل (مثال: ETABS, SAP2000)
    design_software = models.CharField(max_length=255)  # نرم‌افزار طراحی (مثال: SAFE, Tekla)

    structural_drawings = models.FileField(upload_to='structural_design/drawings/', null=True,
                                           blank=True)  # فایل نقشه‌های سازه‌ای
    calculation_report = models.FileField(upload_to='structural_design/reports/', null=True,
                                          blank=True)  # گزارش محاسباتی

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_drawing_file_name(self):
        return self.structural_drawings.name.split('/')[-1]

    def get_report_file_name(self):
        return self.calculation_report.name.split('/')[-1]

    def get_absolute_url(self):
        return reverse('Structure_Design:project_detail', args=[self.slug])


class STRProjectImage(models.Model):
    project = models.ForeignKey(STRProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class STRCoworking(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='bim/video', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # عرض جغرافیایی (lat)
    longitude = models.FloatField(null=True, blank=True)  # طول جغرافیایی (lon)
    pdf = models.FileField(upload_to='bim/pdf', null=True, blank=True)
    image = models.ImageField(upload_to='image/coworking')
    category = models.ForeignKey(STRCategory, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)  # زیربنا (مترمربع)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)  # مساحت زمین (مترمربع)
    usage = models.CharField(max_length=255)  # کاربری (مسکونی، تجاری، اداری و ...)
    num_floors = models.PositiveIntegerField()  # تعداد طبقات
    num_basement_floors = models.PositiveIntegerField()  # تعداد طبقات زیرزمین
    gravity_load_system = models.CharField(max_length=255)  # سیستم باربر ثقلی (مثال: دال بتنی، تیر و ستون فلزی)
    lateral_load_system = models.CharField(max_length=255)  # سیستم باربر جانبی (مثال: قاب خمشی، دیوار برشی)
    project_location = models.CharField(max_length=255)  # مکان پروژه
    construction_year = models.PositiveIntegerField()  # سال ساخت
    parking_capacity = models.PositiveIntegerField()  # تعداد پارکینگ تأمین‌شده
    building_length = models.DecimalField(max_digits=10, decimal_places=2)  # طول ساختمان (متر)
    building_width = models.DecimalField(max_digits=10, decimal_places=2)  # عرض ساختمان (متر)
    floor_height = models.DecimalField(max_digits=5, decimal_places=2)  # ارتفاع طبقات (متر)
    longest_span = models.DecimalField(max_digits=10, decimal_places=2)  # طول بلندترین دهانه (متر)

    material_type = models.CharField(max_length=100, choices=[('Concrete', 'بتنی'), ('Steel', 'فلزی'),
                                                              ('Composite', 'مختلط')])  # نوع مصالح
    foundation_type = models.CharField(max_length=255)  # نوع فونداسیون (مثال: رادیه، نواری، منفرد)
    seismic_design_category = models.CharField(max_length=100)  # دسته‌بندی طراحی لرزه‌ای
    wind_load = models.DecimalField(max_digits=5, decimal_places=2)  # بار باد (kn/m2)
    snow_load = models.DecimalField(max_digits=5, decimal_places=2)  # بار برف (kn/m2)

    design_code = models.CharField(max_length=255)  # آیین‌نامه طراحی (مثال: مبحث ۶، AISC, ASCE 7)
    analysis_software = models.CharField(max_length=255)  # نرم‌افزار تحلیل (مثال: ETABS, SAP2000)
    design_software = models.CharField(max_length=255)  # نرم‌افزار طراحی (مثال: SAFE, Tekla)

    structural_drawings = models.FileField(upload_to='structural_design/drawings/', null=True,
                                           blank=True)  # فایل نقشه‌های سازه‌ای
    calculation_report = models.FileField(upload_to='structural_design/reports/', null=True,
                                          blank=True)  # گزارش محاسباتی

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Structure_Design:coworking_detail", args=[self.slug])

    def get_drawing_file_name(self):
        return self.structural_drawings.name.split('/')[-1]

    def get_report_file_name(self):
        return self.calculation_report.name.split('/')[-1]


class STRCoworkingImage(models.Model):
    coworking = models.ForeignKey(STRCoworking, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coworking_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.coworking.title}"


class STRTraining(BaseModel):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='training_images/')
class EngineeringSoftware(models.Model):
    software_name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    developer = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    supported_platforms = models.CharField(max_length=255)  # مثال: Windows, macOS, Linux
    license_type = models.CharField(max_length=100,
                                    choices=[('Free', 'رایگان'), ('Paid', 'پرداختی'), ('Subscription', 'اشتراکی')])
    features = models.TextField()  # ویژگی‌های نرم‌افزار
    official_website = models.URLField(null=True, blank=True)
    download_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.software_name} ({self.version})"


class ProjectManagement(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)  # نام کارفرما
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # بودجه کل پروژه
    progress_percentage = models.FloatField(default=0.0)  # درصد پیشرفت
    project_status = models.CharField(max_length=100, choices=[('Planning', 'برنامه‌ریزی'), ('Ongoing', 'در حال اجرا'),
                                                               ('Completed', 'تکمیل‌شده')])
    assigned_team = models.TextField(null=True, blank=True)  # اعضای تیم پروژه

    def __str__(self):
        return self.project_name


class RetrofittingProject(models.Model):
    project_name = models.CharField(max_length=255)
    building_age = models.PositiveIntegerField()  # عمر ساختمان (سال)
    current_seismic_resistance = models.CharField(max_length=255, null=True, blank=True)  # مقاومت لرزه‌ای فعلی
    retrofit_strategy = models.TextField()  # استراتژی بهسازی (مثال: ژاکت بتنی، بادبندها، مقاوم‌سازی پی)
    retrofitting_materials = models.TextField(null=True, blank=True)  # مواد مورد استفاده
    expected_performance_level = models.CharField(max_length=255, null=True, blank=True)  # سطح عملکرد پس از بهسازی
    estimated_cost = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # هزینه برآوردی
    retrofit_design_file = models.FileField(upload_to='retrofitting/designs/', null=True,
                                            blank=True)  # فایل طراحی مقاوم‌سازی

    def __str__(self):
        return self.project_name


class BIMProject(models.Model):
    project_name = models.CharField(max_length=255)
    architect = models.CharField(max_length=255, null=True, blank=True)
    structural_engineer = models.CharField(max_length=255, null=True, blank=True)
    contractor = models.CharField(max_length=255, null=True, blank=True)
    bim_software_used = models.CharField(max_length=255, null=True, blank=True)  # مثال: Revit, Tekla
    project_scale = models.CharField(max_length=100,
                                     choices=[('Small', 'کوچک'), ('Medium', 'متوسط'), ('Large', 'بزرگ')])
    model_version = models.CharField(max_length=50, null=True, blank=True)  # نسخه BIM مدل
    is_coordinated = models.BooleanField(default=False)  # آیا مدل هماهنگ‌سازی شده است؟
    total_model_elements = models.IntegerField(null=True, blank=True)  # تعداد عناصر مدل‌شده
    clash_detection_report = models.FileField(upload_to='bim/reports/', null=True, blank=True)  # فایل گزارش تداخلات

    def __str__(self):
        return self.project_name


class StructuralDesignProject(models.Model):
    project_name = models.CharField(max_length=255)  # نام پروژه
    area = models.DecimalField(max_digits=10, decimal_places=2)  # زیربنا (مترمربع)
    land_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # مساحت زمین (مترمربع)
    usage = models.CharField(max_length=255)  # کاربری (مسکونی، تجاری، اداری و ...)
    num_floors = models.PositiveIntegerField()  # تعداد طبقات
    num_basement_floors = models.PositiveIntegerField(null=True, blank=True)  # تعداد طبقات زیرزمین
    gravity_load_system = models.CharField(max_length=255)  # سیستم باربر ثقلی (مثال: دال بتنی، تیر و ستون فلزی)
    lateral_load_system = models.CharField(max_length=255)  # سیستم باربر جانبی (مثال: قاب خمشی، دیوار برشی)
    project_location = models.CharField(max_length=255, null=True, blank=True)  # مکان پروژه
    construction_year = models.PositiveIntegerField(null=True, blank=True)  # سال ساخت
    parking_capacity = models.PositiveIntegerField(null=True, blank=True)  # تعداد پارکینگ تأمین‌شده
    building_length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # طول ساختمان (متر)
    building_width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # عرض ساختمان (متر)
    floor_height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # ارتفاع طبقات (متر)
    longest_span = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                       blank=True)  # طول بلندترین دهانه (متر)

    material_type = models.CharField(max_length=100, choices=[('Concrete', 'بتنی'), ('Steel', 'فلزی'),
                                                              ('Composite', 'مختلط')])  # نوع مصالح
    foundation_type = models.CharField(max_length=255, null=True,
                                       blank=True)  # نوع فونداسیون (مثال: رادیه، نواری، منفرد)
    seismic_design_category = models.CharField(max_length=100, null=True, blank=True)  # دسته‌بندی طراحی لرزه‌ای
    wind_load = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # بار باد (kn/m2)
    snow_load = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # بار برف (kn/m2)

    design_code = models.CharField(max_length=255, null=True,
                                   blank=True)  # آیین‌نامه طراحی (مثال: مبحث ۶، AISC, ASCE 7)
    analysis_software = models.CharField(max_length=255, null=True,
                                         blank=True)  # نرم‌افزار تحلیل (مثال: ETABS, SAP2000)
    design_software = models.CharField(max_length=255, null=True, blank=True)  # نرم‌افزار طراحی (مثال: SAFE, Tekla)

    structural_drawings = models.FileField(upload_to='structural_design/drawings/', null=True,
                                           blank=True)  # فایل نقشه‌های سازه‌ای
    calculation_report = models.FileField(upload_to='structural_design/reports/', null=True,
                                          blank=True)  # گزارش محاسباتی


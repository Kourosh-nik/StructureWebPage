import random
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.db import models
import hashlib
import random
from datetime import timedelta
from django.db import models
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone, email, fullname, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone:
            raise ValueError(_("The phone must be set"))
        email = self.normalize_email(email)
        user = self.model(phone=phone,  email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, email, fullname, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, email, fullname, password, **extra_fields)


class UserModel(PermissionsMixin, AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(_("email address"), blank=True, null=True, unique=True)
    ban = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField('user/profiles', blank=True, null=True)
    register_date = jmodels.jDateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=150, default='No Name')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", 'fullname']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.phone} - {self.fullname}'


class UserFileModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='user/files')
    seen = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    created = jmodels.jDateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.message:
            self.seen = True
        super().save(*args, **kwargs)

    def get_filename(self):
        return self.file.name.split('/')[-1]

class OtpModel(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن', unique=True)
    code = models.CharField(max_length=64, verbose_name='کد هش‌شده')
    attempts = models.IntegerField(default=0, verbose_name='تعداد تلاش‌های ناموفق')
    last_sent_at = models.DateTimeField(auto_now_add=True, verbose_name='آخرین زمان ارسال OTP')
    expires_at = models.DateTimeField(verbose_name='زمان انقضای OTP')

    class Meta:
        verbose_name = 'کد OTP'
        verbose_name_plural = 'کدهای OTP'

    def is_expired(self):
        return now() > self.expires_at

    def reset_attempts(self):
        self.attempts = 0
        self.save()

    @staticmethod
    def generate_otp(phone):
        existing_otp = OtpModel.objects.filter(phone=phone).first()

        if existing_otp and existing_otp.last_sent_at > now() - timedelta(seconds=120):
            return None

        code = random.randint(100000, 999999)
        hashed_code = hashlib.sha256(str(code).encode()).hexdigest()
        expires_at = now() + timedelta(minutes=10)

        if existing_otp:
            existing_otp.code = hashed_code
            existing_otp.expires_at = expires_at
            existing_otp.attempts = 0
            existing_otp.last_sent_at = now()
            existing_otp.save()
        else:
            OtpModel.objects.create(phone=phone, code=hashed_code, expires_at=expires_at, last_sent_at=now())

        return code

    def verify_otp(self, input_code):
        if self.is_expired():
            self.delete()
            return False

        if self.attempts >= 5:
            self.delete()
            return False

        hashed_input = hashlib.sha256(str(input_code).encode()).hexdigest()
        if hashed_input == self.code:
            self.delete()
            return True

        self.attempts += 1
        self.save()
        return False



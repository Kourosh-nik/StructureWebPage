import random
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinLengthValidator


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
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    code = models.CharField(max_length=11, verbose_name='کد')
    date = models.DateTimeField(auto_now_add=True, verbose_name='انقضا')

    class Meta:
        verbose_name = 'کد OTP'
        verbose_name_plural = 'کد OTP'
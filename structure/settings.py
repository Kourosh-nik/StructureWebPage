import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'bifdsfiuwhf7$%fnds#@^^$%^@^T$#TGDFLGERGL%'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # LOCAL APPS
    'structure',
    'Apps.Home_Page',
    'Apps.Structure_Design',
    'Apps.BIM.apps.BimConfig',
    'Apps.project_management',
    'Apps.Retrofit',
    'Apps.Software',
    'Apps.Users',

    # EXTERNAL APPS
    'django_render_partial',
    'django_jalali',
]

AUTH_USER_MODEL = 'Users.UserModel'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'structure.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'structure.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ketec',
        'USER': 'ketec',
        'PASSWORD': 'ketec',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}
#
# LIARA CONFIG
AWS_ACCESS_KEY_ID = 's7mtd3ecb1safiaq'
AWS_SECRET_ACCESS_KEY = '50dfce50-11b3-45a6-a8ec-4029430c8ae5'
AWS_STORAGE_BUCKET_NAME = 'akurtek'
AWS_S3_ENDPOINT_URL = 'https://storage.c2.liara.space'
AWS_S3_REGION_NAME = 'us-east-1'

# AWS_ACCESS_KEY_ID = '5de4b746-59da-4a18-bec9-411c09793550'
# AWS_SECRET_ACCESS_KEY = '334a4bf4798191fc2f26ace1cde01b68ab00556d1c43285f49cbccc8e6b4304d'
# AWS_STORAGE_BUCKET_NAME = 'ketec'
# AWS_S3_ENDPOINT_URL = 'https://ketec.s3.ir-thr-at1.arvanstorage.ir'
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.ir-thr-at1.arvanstorage.com"
#
# # تنظیم ذخیره فایل‌های رسانه‌ای در آروان
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

USE_TZ = True
STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

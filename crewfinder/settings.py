"""
Django settings for crewfinder project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""



from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
import sys

import cloudinary
from cloudinary import config




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j7o9m0=b+=n@u^rv&kldm56ry0%@1da1afjcy^m(02jq=qe0i-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['8000-doylekfd-crewfinder-18t8urmmyig.ws.codeinstitute-ide.net',
                 '.herokuapp.com']

SECRET_KEY = os.environ.get("SECRET_KEY")

CSRF_TRUSTED_ORIGINS = [
    'https://8000-doylekfd-crewfinder-18t8urmmyig.ws.codeinstitute-ide.net',
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com",
    "https://ui.dev/"
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',  # Required by Allauth
    'allauth',               # Required by Allauth
    'allauth.account',       # Required by Allauth
    'crispy_forms',          # Required for Crispy Forms
    'crispy_bootstrap5',     # Required for Crispy Forms
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'trips',
    'crewbooking',
    'cloudinary',
    'cloudinary_storage',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',            # Django default backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth backend
)




LOGIN_REDIRECT_URL = '/accounts/dashboard/'  # Where to go after login
LOGOUT_REDIRECT_URL = '/'  # Where to go after logout
ACCOUNT_ADAPTER = 'accounts.adapter.CustomAccountAdapter'
ACCOUNT_LOGIN_ON_SIGNUP = False  # Ensure that users are not logged in automatically after signup
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/registration_pending/'
ACCOUNT_INACTIVE_REDIRECT_URL = '/accounts/registration_pending/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/login/'


CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Moved up
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'accounts.middleware.ProfileCompletionMiddleware',  # Custom profile completion
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crewfinder.urls'

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

WSGI_APPLICATION = 'crewfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Use SQLite for tests to avoid permission issues
# if 'test' in sys.argv:
#    DATABASES['default'] = {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': ':memory:',  # Creates a temporary in-memory database
#    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
}

def custom_login_view(request):
    if request.user.role == User.ADMINISTRATOR:
        return redirect('admin_dashboard')
    return redirect('dashboard')

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

SITE_URL = os.environ.get('SITE_URL', 'https://8000-doylekfd-crewfinder-18t8urmmyig.ws.codeinstitute-ide.net/')

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
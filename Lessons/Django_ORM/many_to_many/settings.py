from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(=bl_n5qake0pytas@46&mbsh7btp)co!(#wj*t+c)(8@pyf+n'

# Application definition
INSTALLED_APPS = [
    "db",
    "django_extensions"
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
LANGUAGE_CODE = 'en-us'
USE_TZ = False

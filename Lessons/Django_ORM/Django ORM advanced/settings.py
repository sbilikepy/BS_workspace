
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-w4^ow=%1=2e5%sifu%qm1rya=xz6=rco7nx4!!1_t5ot1ai(3h'


INSTALLED_APPS = [
<<<<<<< HEAD
    "bus_station",
    "django_extensions"
=======
    'bus_station'
>>>>>>> e105492d111a88feb65c4f7d51e4d6554ce7df4a
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = False


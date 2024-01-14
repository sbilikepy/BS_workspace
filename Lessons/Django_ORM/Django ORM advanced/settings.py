from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "django-insecure-w4^ow=%1=2e5%sifu%qm1rya=xz6=rco7nx4!!1_t5ot1ai(3h"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "bus_station",
    "django_extensions",
]

AUTH_USER_MODEL = "bus_station.User"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_TZ = False

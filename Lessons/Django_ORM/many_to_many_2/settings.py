from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "django-insecure-#0qyv59rg*=m+=+tozc(27d6-p6$*p%v8j#wh*&q7n-=j^7g_k"


# Application definition

INSTALLED_APPS = ["db"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = False

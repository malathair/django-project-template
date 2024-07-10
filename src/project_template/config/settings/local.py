import environ
import os

from django.core.management.utils import get_random_secret_key
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECRET_KEY = (
    env("DJANGO_SECRET")
    if not DEBUG
    else env("DJANGO_SECRET", default=get_random_secret_key()
)
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", default=list())

if env.str("DATABASE_URL", default=""):
    DATABASES = {"default": env.db()}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

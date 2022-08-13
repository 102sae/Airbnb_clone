from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER_MALE = "male"
GENDER_FEMALE = "female"
GENDER_OTHER = "other"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "female"),
    (GENDER_OTHER, "other"),
)

LANG_ENG = "en"
LANG_KOR = "kr"

LANG_CHOICE = ((LANG_ENG, "English"), (LANG_KOR, "korean"))

CURRENCY_USD = "usd"
CURRENCY_KRW = "krw"

CURRENCY_CHOICE = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))


class User(AbstractUser):
    """Custom User Model"""

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    language = models.CharField(choices=LANG_CHOICE, max_length=2, blank=True)

    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)

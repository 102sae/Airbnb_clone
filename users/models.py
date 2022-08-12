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

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)

    birthdate = models.DateField(null=True)

    language = models.CharField(
        choices=LANG_CHOICE, max_length=2, null=True, blank=True
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)

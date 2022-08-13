from turtle import update
from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # model이 생성할때마다 date, time 기록
    updated = models.DateTimeField(auto_now=True)  # model을 저장할때마다 date와 time 기록

    class Meta:
        abstract = True
        # 추상 클래스는 데이터베이스에 저장안됨

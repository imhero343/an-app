from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField('الاسم',  max_length=200, default="")
    direction = models.CharField('التوجه', max_length=200, default="")
    represent = models.CharField('الموقعية', max_length=200, default="")
    age = models.IntegerField('العمر', default=0)
    gov = models.CharField('المحافظة', max_length=200, default="")
    area = models.CharField('المنطقة', max_length=200, default="")
    phone = models.CharField('رقم الهاتف', max_length=200, default="")
    nkown_person = models.CharField(
        'الشخص المعروف', max_length=200, default="")
    nkown_person_phone = models.CharField(
        'رقم الشخص المعروف', max_length=200, default="")
    nkown_person_relation = models.CharField(
        'مقدار علاقة الشخص بالمعرف', max_length=200, default="")
    notes = models.TextField(
        'الملاحظات', max_length=200, default="")

    def __str__(self):
        return self.name

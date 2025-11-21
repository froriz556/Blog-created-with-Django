from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, EmailField, CharField

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('У пользователя должен быть email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    email = EmailField(unique=True)
    username = CharField(unique=True, max_length=30)
    email_confirmed = BooleanField(default=False)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username or 'Нет имени'} — {self.email}"


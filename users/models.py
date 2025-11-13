from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователь. Содержит поля email, phone, birthdate, created_at, updated_at."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")

    phone = models.CharField(max_length=35, verbose_name="Телефон", blank=True, null=True)
    birthdate = models.DateField(verbose_name="Дата рождения", help_text="Укажите дату рождения", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, {self.is_active}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

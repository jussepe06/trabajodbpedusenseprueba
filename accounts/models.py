from django.contrib.auth.models import AbstractUser
from django.db import models


class University(models.Model):
    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )

    email_domain = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    logo = models.URLField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('STUDENT', 'Estudiante'),
        ('COUNSELOR', 'Orientador'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='STUDENT'
    )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='users',
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        university_name = self.university.name if self.university else "Sin universidad"
        return f"{self.username} - {self.role} - {university_name}"
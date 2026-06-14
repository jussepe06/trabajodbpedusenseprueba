from django.db import models
from accounts.models import User, University


class StudentProfile(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Bajo'),
        ('MODERATE', 'Moderado'),
        ('HIGH', 'Alto'),
        ('CRITICAL', 'Crítico'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='students'
    )

    student_code = models.CharField(
        max_length=20,
        unique=True
    )

    faculty = models.CharField(
        max_length=100
    )

    career = models.CharField(
        max_length=100
    )

    age = models.IntegerField()

    emotional_score = models.IntegerField(
        default=0
    )

    risk_level = models.CharField(
        max_length=20,
        choices=RISK_LEVELS,
        default='LOW'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.risk_level}"


class EmotionalCheckin(models.Model):
    MOOD_CHOICES = [
        ('VERY_GOOD', 'Muy bien'),
        ('GOOD', 'Bien'),
        ('NEUTRAL', 'Regular'),
        ('BAD', 'Mal'),
        ('VERY_BAD', 'Muy mal'),
    ]

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='checkins'
    )

    mood = models.CharField(
        max_length=20,
        choices=MOOD_CHOICES
    )

    stress_level = models.IntegerField()

    sleep_hours = models.IntegerField()

    motivation_level = models.IntegerField()

    feels_supported = models.BooleanField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.created_at.date()}"
from django.db import models
from students.models import StudentProfile


class Alert(models.Model):
    RISK_LEVELS = (
        ('LOW', 'Bajo'),
        ('MODERATE', 'Moderado'),
        ('HIGH', 'Alto'),
        ('CRITICAL', 'Crítico'),
    )

    STATUS = (
        ('PENDING', 'Pendiente'),
        ('IN_PROGRESS', 'En proceso'),
        ('RESOLVED', 'Resuelta'),
    )

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='alerts'
    )

    risk_level = models.CharField(
        max_length=20,
        choices=RISK_LEVELS
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='PENDING'
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.risk_level}"
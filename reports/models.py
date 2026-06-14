from django.db import models
from students.models import StudentProfile


class Report(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    summary = models.TextField()

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Reporte - {self.student.user.username}"
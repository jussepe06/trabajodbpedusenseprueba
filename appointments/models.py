from django.db import models
from students.models import StudentProfile
from accounts.models import User


class Appointment(models.Model):
    STATUS = (
        ('SCHEDULED', 'Programada'),
        ('COMPLETED', 'Completada'),
        ('CANCELLED', 'Cancelada'),
    )

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE
    )

    counselor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'COUNSELOR'}
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    observations = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='SCHEDULED'
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.appointment_date}"
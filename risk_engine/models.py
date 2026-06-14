from django.db import models


class RiskRule(models.Model):
    risk_name = models.CharField(max_length=100)
    min_attendance = models.DecimalField(max_digits=5, decimal_places=2)
    min_average = models.DecimalField(max_digits=4, decimal_places=2)
    min_participation = models.DecimalField(max_digits=5, decimal_places=2)
    risk_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.risk_name} - {self.risk_level}"
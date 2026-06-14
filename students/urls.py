from django.urls import path
from .views import student_checkin, student_history


urlpatterns = [
    path('student-checkin/', student_checkin, name='student_checkin'),
    path('student-history/', student_history, name='student_history'),
]
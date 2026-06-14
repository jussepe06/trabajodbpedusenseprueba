from django.urls import path
from .views import (
    request_appointment,
    my_appointments,
    counselor_appointments
)

urlpatterns = [
    path('request/', request_appointment, name='request_appointment'),
    path('my/', my_appointments, name='my_appointments'),
    path('counselor/', counselor_appointments, name='counselor_appointments'),
]
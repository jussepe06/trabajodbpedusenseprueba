from django.urls import path
from .views import counselor_alerts


urlpatterns = [
    path('counselor/', counselor_alerts, name='counselor_alerts'),
]
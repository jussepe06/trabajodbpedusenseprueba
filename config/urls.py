from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from students.models import StudentProfile
from alerts.models import Alert
from appointments.models import Appointment

def landing(request):
    return render(request, 'landing.html')


def student_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if request.user.role != 'STUDENT':
        return redirect('/')

    student = StudentProfile.objects.get(user=request.user)

    context = {
        'student': student
    }

    return render(request, 'student_dashboard.html', context)


def counselor_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if request.user.role != 'COUNSELOR':
        return redirect('/')

    students = StudentProfile.objects.filter(
        university=request.user.university
    )

    alerts = Alert.objects.filter(
        student__university=request.user.university
    )

    appointments = Appointment.objects.filter(
        counselor=request.user
    )

    critical_alerts = alerts.filter(
        risk_level='CRITICAL'
    ).count()

    moderate_alerts = alerts.filter(
        risk_level='MODERATE'
    ).count()

    context = {
        'students': students,
        'alerts': alerts,
        'appointments': appointments,
        'critical_alerts': critical_alerts,
        'moderate_alerts': moderate_alerts,
    }

    return render(request, 'counselor_dashboard.html', context)


def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if request.user.role != 'ADMIN':
        return redirect('/')

    return render(request, 'admin_dashboard.html')


urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('counselor-dashboard/', counselor_dashboard, name='counselor_dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('students/', include('students.urls')),
    path('appointments/', include('appointments.urls')),
    path('alerts/', include('alerts.urls')),
]
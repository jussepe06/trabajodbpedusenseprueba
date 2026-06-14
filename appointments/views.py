from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import StudentProfile
from accounts.models import User
from .models import Appointment


@login_required
def request_appointment(request):
    if request.user.role != 'STUDENT':
        return redirect('/')

    student = StudentProfile.objects.get(
        user=request.user
    )

    counselors = User.objects.filter(
        role='COUNSELOR',
        university=request.user.university
    )

    if request.method == 'POST':
        Appointment.objects.create(
            student=student,
            counselor_id=request.POST.get('counselor'),
            appointment_date=request.POST.get('appointment_date'),
            appointment_time=request.POST.get('appointment_time'),
            observations=request.POST.get('observations')
        )

        return redirect('/student-dashboard/')

    context = {
        'counselors': counselors
    }

    return render(
        request,
        'request_appointment.html',
        context
    )


@login_required
def my_appointments(request):
    if request.user.role != 'STUDENT':
        return redirect('/')

    student = StudentProfile.objects.get(
        user=request.user
    )

    appointments = Appointment.objects.filter(
        student=student
    ).order_by('-appointment_date')

    context = {
        'appointments': appointments
    }

    return render(
        request,
        'my_appointments.html',
        context
    )
@login_required
def counselor_appointments(request):
    if request.user.role != 'COUNSELOR':
        return redirect('/')

    if request.method == 'POST':
        appointment = Appointment.objects.get(
            id=request.POST.get('appointment_id')
        )

        appointment.status = request.POST.get('status')
        appointment.save()

    appointments = Appointment.objects.filter(
        counselor=request.user
    ).order_by('appointment_date')

    context = {
        'appointments': appointments
    }

    return render(
        request,
        'counselor_appointments.html',
        context
    )
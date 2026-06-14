from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, EmotionalCheckin


@login_required
def student_checkin(request):
    if request.user.role != 'STUDENT':
        return redirect('/')

    if request.method == 'POST':
        student = StudentProfile.objects.get(
            user=request.user
        )

        EmotionalCheckin.objects.create(
            student=student,
            mood=request.POST.get('mood'),
            stress_level=request.POST.get('stress_level'),
            sleep_hours=request.POST.get('sleep_hours'),
            motivation_level=request.POST.get('motivation_level'),
            feels_supported=request.POST.get('feels_supported') == 'true',
            notes=request.POST.get('notes')
        )

        return redirect('/student-dashboard/')

    return render(request, 'student_checkin.html')


@login_required
def student_history(request):
    if request.user.role != 'STUDENT':
        return redirect('/')

    student = StudentProfile.objects.get(
        user=request.user
    )

    checkins = EmotionalCheckin.objects.filter(
        student=student
    ).order_by('-created_at')

    context = {
        'student': student,
        'checkins': checkins
    }

    return render(
        request,
        'student_history.html',
        context
    )
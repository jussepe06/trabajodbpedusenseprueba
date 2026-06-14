from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Alert


@login_required
def counselor_alerts(request):
    if request.user.role != 'COUNSELOR':
        return redirect('/')

    if request.method == 'POST':
        alert = Alert.objects.get(
            id=request.POST.get('alert_id')
        )

        alert.status = request.POST.get('status')
        alert.save()

    alerts = Alert.objects.filter(
        student__university=request.user.university
    ).order_by('-created_at')

    context = {
        'alerts': alerts
    }

    return render(
        request,
        'counselor_alerts.html',
        context
    )
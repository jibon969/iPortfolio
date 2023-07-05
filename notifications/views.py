from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from django.contrib import messages


def notification_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        notifications = Notification.objects.filter(user=request.user).order_by('-id')
        return render(request, 'notification/notification.html', {'notifications': notifications})
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('home')




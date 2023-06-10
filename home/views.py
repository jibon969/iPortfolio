from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactForm
from django.contrib import messages


def home(request):
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, "home/index.html", context)

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ContactForm
from django.contrib import messages


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            messages.add_message(request, messages.WARNING, "Please try again !")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ContactForm()
    context = {
        'from': form,
    }
    return render(request, "home/index.html", context)

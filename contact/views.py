from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank you for your message. i will respond as soon as possible.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.WARNING, "Please try again !")
            return render(request, "contact/contact.html", {'form': form})
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})

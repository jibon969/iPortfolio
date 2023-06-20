from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .forms import RegisterForm, LoginForm


# Create your views
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registration Successfully Completed')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

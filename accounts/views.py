from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, UserProfileForm
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registration Successfully Completed')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}")
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.WARNING, "You are successfully logout !")
    return redirect('accounts:login')


def profile_view(request):
    form = UserProfileForm(instance=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)  # Create unsaved instance
            # Modify the profile if needed
            # For example: profile.bio = form.cleaned_data['bio']
            profile.save()  # Save the modified profile
            messages.success(request, 'Profile successfully updated')
            return redirect('home')
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('registration/', views.register_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Change Password !
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/registration/password_change_done.html'), name='password_change_done'),

    
    # Password Reset urls.py
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/registration/password_reset.html',
        email_template_name='accounts/registration/password_reset_email.html',
        subject_template_name='accounts/registration/password_reset_subject.txt'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/registration/password_reset_complete.html'), name='password_reset_complete'),


]

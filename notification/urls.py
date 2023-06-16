from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('notifications/', views.notifications, name="notifications"),

    path('expenses/', views.expense_list, name='expense_list'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('expenses/<int:expense_id>/update/', views.update_expense, name='update_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
]

from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Notification
from .forms import ExpenseForm


def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-id')
    return render(request, 'notification/notifications.html', {'notifications': notifications})


def dashboard(request):
    unread_notifications = Notification.objects.filter(user=request.user, read=False).count()
    return render(request, 'notification/dashboard.html', {'unread_notifications': unread_notifications})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'notification/expense_list.html', {'expenses': expenses})


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # Create the expense
            expense = Expense(name=name)
            expense.save()

            # Create a notification for the user
            notification_message = f'New expense created: {name}'
            link = "http://127.0.0.1:8000/expenses/"  # Set the appropriate link if needed
            # link = None  # Set the appropriate link if needed
            notification = Notification(user=request.user, message=notification_message, link=link)
            notification.save()

            return redirect('dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'notification/create_expense.html', {'form': form})


def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()

            # Update the associated notification message
            notification = Notification.objects.get(user=request.user, message__contains=expense.name)
            notification.message = f'Expense updated: {expense.name}'
            notification.save()

            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'notification/update_expense.html', {'form': form, 'expense': expense})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Delete the associated notification messages
    notifications = Notification.objects.filter(user=request.user, message__contains=expense.name)
    notifications.delete()

    # Delete the expense object
    expense.delete()
    return redirect('expense_list')
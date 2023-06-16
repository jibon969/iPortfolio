from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    name = models.CharField(max_length=120)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notification")
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    read = models.BooleanField(default=False)

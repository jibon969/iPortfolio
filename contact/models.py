from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-created_at']


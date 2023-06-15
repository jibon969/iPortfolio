from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
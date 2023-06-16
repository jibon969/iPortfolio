from django.db import models


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=120)
    status = models.CharField(max_length=150)
    image = models.FileField()
    resume = models.FileField()

    def __str__(self):
        return self.name


class AboutSkill(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

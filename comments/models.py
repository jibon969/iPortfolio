from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Replay(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='replays')
    body = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)

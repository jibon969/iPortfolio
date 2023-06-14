from django.db import models
from django.db.models.signals import pre_save
from .utils import blog_unique_slug_generator


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)


class Blog(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to="blog/", blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def blog_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = blog_unique_slug_generator(instance)


pre_save.connect(blog_pre_save_receiver, sender=Blog)



class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.name)

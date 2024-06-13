from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to='blog/static/images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ClientInfo(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

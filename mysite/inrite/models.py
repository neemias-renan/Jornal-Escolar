from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Edition(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    contact_info = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    description = models.TextField(null=True)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='news/', null=True, default="")
    date = models.DateTimeField('date_publish', default = timezone.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

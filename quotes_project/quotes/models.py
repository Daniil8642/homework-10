from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
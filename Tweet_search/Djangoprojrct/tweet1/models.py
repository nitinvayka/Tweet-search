from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}..."  # Display first 20 characters of the tweet

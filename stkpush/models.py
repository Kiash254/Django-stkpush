from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.user.username

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/', default='cards/default.png')

    def __str__(self):
        return self.title

class AppointmentBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ofc_location = models.CharField(max_length=100, default='ANY')
    consular_location = models.CharField(max_length=100, default='DELHI')
    preferred_time = models.TimeField()

    def __str__(self):
        return f"Bot for {self.user.username}"
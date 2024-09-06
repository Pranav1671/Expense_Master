from django.db import models
from django.utils import timezone


class YourModel(models.Model):
    # other fields...
    new_field = models.DateTimeField(default=timezone.now)

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField()

    class Meta:
        db_table = "user"

class UserProfile1(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True, default=None)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True, default=None)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default=None)
    logpass = models.CharField(max_length=100, default=123456, blank=True)

    class Meta:
        db_table = "profile"
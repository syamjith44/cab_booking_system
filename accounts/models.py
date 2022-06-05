from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50)


class DriverRegistrations(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Verified', 'Verified')
    )
    mobile = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=100, null=True)
    profile_img = models.ImageField(upload_to='profile_images')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    driving_licence = models.ImageField(upload_to='driving_licenses')
    vehicle_registration = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Pending')


class DriverUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    profile_img = models.ImageField(upload_to='profile_images')
    age = models.PositiveIntegerField()
    driving_licence = models.ImageField(upload_to='driving_licenses')
    vehicle_registration = models.CharField(max_length=15)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)


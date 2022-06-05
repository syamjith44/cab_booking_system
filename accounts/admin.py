from django.contrib import admin
from .models import DriverRegistrations, City, DriverUser


admin.site.register(City)
admin.site.register(DriverRegistrations)
admin.site.register(DriverUser)
# Register your models here.
from django.contrib import admin

from .models import Instructor, Reservation

admin.site.register(Instructor)
admin.site.register(Reservation)
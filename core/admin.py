# Register your models here.
from django.contrib import admin

from .models import Instructor, Reservation, AvailableDate

admin.site.register(Instructor)
admin.site.register(Reservation)
admin.site.register(AvailableDate)
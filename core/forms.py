from django import forms
from .models import Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "instructor",
            "customer_name",
            "reservation_date",
        ]

        widgets = {
            "instructor": forms.Select(
                attrs={
                    "hx-get": "/available-dates/",
                    "hx-trigger": "change",
                    "hx-target": "#available",
                }
            ),
            "reservation_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
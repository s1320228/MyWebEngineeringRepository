from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Reservation


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


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
                    "class": "form-select",
                    "hx-get": "/available-dates/",
                    "hx-trigger": "change",
                    "hx-target": "#available",
                    "hx-swap": "innerHTML",
                    "hx-indicator": "#date-loading",
                }
            ),
            "customer_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "autocomplete": "name",
                }
            ),
            "reservation_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data["reservation_date"]

        if reservation_date < date.today():
            raise ValidationError(
                "You cannot make a reservation for a past date."
            )

        return reservation_date
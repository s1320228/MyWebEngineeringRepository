from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Reservation, AvailableDate


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

    def clean(self) :
        cleaned_date = super().clean()
        instructor = cleaned_date.get("instructor")
        reservation_date = cleaned_date.get("reservation_date")

        if instructor and reservation_date :
            if not AvailableDate.objects.filter(
                instructor = instructor,
                date = reservation_date
            ).exists() :
                raise forms.ValidationError(
                    "Please select one of the available dates for this instructor."
                    )
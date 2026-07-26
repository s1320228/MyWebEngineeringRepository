from django import forms
from .models import Reservation


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
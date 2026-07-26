import pytest

from core.forms import ReservationForm
from core.models import Instructor


@pytest.mark.django_db
def test_reservation_form_is_valid():
    instructor = Instructor.objects.create(name="Alice")

    form = ReservationForm(
        data={
            "instructor": instructor.id,
            "customer_name": "John",
            "reservation_date": "2026-08-01",
        }
    )

    assert form.is_valid()


@pytest.mark.django_db
def test_reservation_form_rejects_empty_customer_name():
    instructor = Instructor.objects.create(name="Alice")

    form = ReservationForm(
        data={
            "instructor": instructor.id,
            "customer_name": "",
            "reservation_date": "2026-08-01",
        }
    )

    assert not form.is_valid()
    assert "customer_name" in form.errors


@pytest.mark.django_db
def test_reservation_form_rejects_empty_date():
    instructor = Instructor.objects.create(name="Alice")

    form = ReservationForm(
        data={
            "instructor": instructor.id,
            "customer_name": "John",
            "reservation_date": "",
        }
    )

    assert not form.is_valid()
    assert "reservation_date" in form.errors
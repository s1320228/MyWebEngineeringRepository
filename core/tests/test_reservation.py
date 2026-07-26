import pytest
from core.models import Instructor, Reservation

@pytest.mark.django_db
def test_create_reservation():
    instructor = Instructor.objects.create(
        name="Alice"
    )

    reservation = Reservation.objects.create(
        instructor=instructor,
        customer_name="John",
        reservation_date="2026-08-01"
    )

    assert reservation.customer_name == "John"
    assert reservation.instructor == instructor
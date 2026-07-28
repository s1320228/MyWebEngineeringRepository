from datetime import date, timedelta

import pytest
from django.contrib.auth.models import User

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

@pytest.mark.django_db
def test_reservation_is_related_to_user_and_instructor():
    user = User.objects.create_user(
        username="alice",
        password="password123",
    )
    instructor = Instructor.objects.create(name="Emma")

    reservation = Reservation.objects.create(
        user=user,
        instructor=instructor,
        customer_name="Alice",
        reservation_date=date.today() + timedelta(days=7),
    )

    assert reservation.user == user
    assert reservation.instructor == instructor
from datetime import date

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from core.models import AvailableDate, Instructor, Reservation


@pytest.mark.django_db
def test_home_page(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "Royal Dance School" in response.content.decode()


@pytest.mark.django_db
def test_instructor_list_page(client):
    Instructor.objects.create(name="Alice")

    response = client.get(reverse("instructor_list"))

    assert response.status_code == 200
    assert "Alice" in response.content.decode()


@pytest.mark.django_db
def test_reservation_requires_login(client):
    response = client.get(reverse("reservation"))

    assert response.status_code == 302
    assert reverse("login") in response.url


@pytest.mark.django_db
def test_logged_in_user_can_open_reservation_page(client):
    user = User.objects.create_user(
        username="john",
        password="password123",
    )

    client.force_login(user)

    response = client.get(reverse("reservation"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_logged_in_user_can_create_reservation(client):
    user = User.objects.create_user(
        username="john",
        password="password123",
    )

    instructor = Instructor.objects.create(
        name="Alice",
    )

    client.force_login(user)

    response = client.post(
        reverse("reservation"),
        {
            "instructor": instructor.id,
            "customer_name": "John",
            "reservation_date": "2026-08-01",
        },
    )

    assert response.status_code == 302
    assert response.url == reverse("my_reservations")
    assert Reservation.objects.count() == 1

    reservation = Reservation.objects.first()

    assert reservation is not None
    assert reservation.customer_name == "John"
    assert reservation.instructor == instructor
    assert reservation.user == user
    assert reservation.reservation_date == date(2026, 8, 1)


@pytest.mark.django_db
def test_invalid_reservation_is_not_saved(client):
    user = User.objects.create_user(
        username="john",
        password="password123",
    )

    instructor = Instructor.objects.create(
        name="Alice",
    )

    client.force_login(user)

    response = client.post(
        reverse("reservation"),
        {
            "instructor": instructor.id,
            "customer_name": "",
            "reservation_date": "2026-08-01",
        },
    )

    assert response.status_code == 200
    assert Reservation.objects.count() == 0


@pytest.mark.django_db
def test_available_dates_returns_dates_for_selected_instructor(
    client,
):
    instructor = Instructor.objects.create(
        name="Alice",
    )

    AvailableDate.objects.create(
        instructor=instructor,
        date=date(2026, 8, 1),
    )

    AvailableDate.objects.create(
        instructor=instructor,
        date=date(2026, 8, 5),
    )

    response = client.get(
        reverse("available_dates"),
        {"instructor": instructor.id},
        HTTP_HX_REQUEST="true",
    )

    content = response.content.decode()

    assert response.status_code == 200
    assert "2026-08-01" in content
    assert "2026-08-05" in content


@pytest.mark.django_db
def test_available_dates_does_not_return_other_instructor_dates(
    client,
):
    instructor_one = Instructor.objects.create(
        name="Alice",
    )

    instructor_two = Instructor.objects.create(
        name="Bob",
    )

    AvailableDate.objects.create(
        instructor=instructor_one,
        date=date(2026, 8, 1),
    )

    AvailableDate.objects.create(
        instructor=instructor_two,
        date=date(2026, 8, 3),
    )

    response = client.get(
        reverse("available_dates"),
        {"instructor": instructor_one.id},
        HTTP_HX_REQUEST="true",
    )

    content = response.content.decode()

    assert response.status_code == 200
    assert "2026-08-01" in content
    assert "2026-08-03" not in content


@pytest.mark.django_db
def test_available_dates_handles_missing_instructor(client):
    response = client.get(
        reverse("available_dates"),
        HTTP_HX_REQUEST="true",
    )

    content = response.content.decode()

    assert response.status_code == 200
    assert "Select an instructor" in content
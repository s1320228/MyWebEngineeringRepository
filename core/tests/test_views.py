import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from core.models import Instructor, Reservation


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
    User.objects.create_user(
        username="john",
        password="password123",
    )

    client.login(
        username="john",
        password="password123",
    )

    response = client.get(reverse("reservation"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_logged_in_user_can_create_reservation(client):
    User.objects.create_user(
        username="john",
        password="password123",
    )

    instructor = Instructor.objects.create(name="Alice")

    client.login(
        username="john",
        password="password123",
    )

    response = client.post(
        reverse("reservation"),
        {
            "instructor": instructor.id,
            "customer_name": "John",
            "reservation_date": "2026-08-01",
        },
    )

    assert response.status_code == 200
    assert Reservation.objects.count() == 1

    reservation = Reservation.objects.first()

    assert reservation is not None
    assert reservation.customer_name == "John"
    assert reservation.instructor == instructor


@pytest.mark.django_db
def test_invalid_reservation_is_not_saved(client):
    User.objects.create_user(
        username="john",
        password="password123",
    )

    instructor = Instructor.objects.create(name="Alice")

    client.login(
        username="john",
        password="password123",
    )

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
def test_available_dates(client):
    response = client.get(
        reverse("available_dates"),
        {"instructor": "1"},
    )

    assert response.status_code == 200
    assert "2026-07-28" in response.content.decode()
import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_register_page(client):
    response = client.get(reverse("register"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_register(client):
    response = client.post(
        reverse("register"),
        {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        },
    )

    assert response.status_code == 302
    assert User.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_login_page(client):
    response = client.get(reverse("login"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_can_login(client):
    User.objects.create_user(
        username="john",
        password="password123",
    )

    response = client.post(
        reverse("login"),
        {
            "username": "john",
            "password": "password123",
        },
    )

    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_requires_post(client):
    User.objects.create_user(
        username="john",
        password="password123",
    )

    client.login(
        username="john",
        password="password123",
    )

    response = client.get(reverse("logout"))

    assert response.status_code == 405


@pytest.mark.django_db
def test_user_can_logout_with_post(client):
    User.objects.create_user(
        username="john",
        password="password123",
    )

    client.login(
        username="john",
        password="password123",
    )

    response = client.post(reverse("logout"))

    assert response.status_code == 302
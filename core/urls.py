from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path(
        "", 
        views.home, 
        name="home"
    ),
    path(
        "objects/", 
        views.object_list, 
        name="object_list"
    ),
    path(
        "process/", 
        views.process_request, 
        name="process_request"
    ),
    path(
        "redirect/", 
        views.go_home, 
        name="go_home"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login",
    ),
    path(
        "logout/", 
        auth_views.LogoutView.as_view(), 
        name="logout"
    ),
    path(
        "reservation/", 
        views.reservation, 
        name="reservation"
    ),
    path(
        "register/", 
        views.register, 
        name="register"
    ),
    path(
        "available-dates/", 
        views.available_dates,
        name="available_dates",
    ),
    path(
        "instructors/", 
        views.instructor_list, 
        name="instructor_list"
    ),
    path(
        "reservation/success/",
        views.reservation_success,
        name="reservation_success",
    ),
    path(
        "my-reservations/",
        views.my_reservations,
        name="my_reservations",
    ),
    path(
        "reservations/<int:reservation_id>/edit/",
        views.edit_reservation,
        name="edit_reservation",
    ),
    path(
        "reservations/<int:reservation_id>/cancel/",
        views.cancel_reservation,
        name="cancel_reservation",
    ),
    path(
        "available-dates/",
        views.available_dates,
        name="available_dates"
    ),
    # Password reset form
    path(
        "password_reset/", 
        auth_views.PasswordResetView.as_view(),
        name="password_reset"
    ),
    # Password reset mail is sent
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    # Change password
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change"
    ),
    # Reset password
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    # Completed password reset
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_completed"
    ),
]
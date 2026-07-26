from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("objects/", views.object_list, name="object_list"),
    path("process/", views.process_request, name="process_request"),
    path("redirect/", views.go_home, name="go_home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login",
    ),
    path("reservation/", views.reservation, name="reservation"),
    path("register/", views.register, name="register"),
    path("available-dates/", views.available_dates,name="available_dates",),
    path("instructors/", views.instructor_list, name="instructor_list"),
    path("register/", views.register, name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout",),
]
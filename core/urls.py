from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("objects/", views.object_list, name="object_list"),
    path("process/", views.process_request, name="process_request"),
    path("redirect/", views.go_home, name="go_home"),
    path("login/", views.login_view, name="login"),
    path("reservation/", views.reservation, name="reservation"),
    path("register/", views.register, name="register"),
    path("available-dates/", views.available_dates,name="available_dates",),
]
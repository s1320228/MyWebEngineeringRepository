from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "objects/",
        views.object_list,
        name="object_list"
    ),

    path(
        "form/",
        views.form_page,
        name="form_page"
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
]
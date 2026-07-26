# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReservationForm, RegisterForm
from .models import Instructor
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def object_list(request):
    return HttpResponse("Object List")


def form_page(request):
    return HttpResponse("Form Page")


def process_request(request):
    return HttpResponse("Processed")

@login_required
def reservation(request) :
    if request.method == "POST" :
        form = ReservationForm(request.POST)

        if form.is_valid() :
            form.save()
            return render(request, "success.html")
    else :
        form = ReservationForm()

    return render(request, "reservation.html", {"form":form},)

def login_view(request) :
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "register.html",
        {"form": form},
    )

def go_home(request):
    return redirect("/")

def available_dates(request):
    instructor = request.GET.get("instructor")

    dates = []

    if instructor == "1":
        dates = [
            "2026-07-28",
            "2026-07-29",
            "2026-07-31",
        ]
    elif instructor == "2":
        dates = [
            "2026-07-30",
            "2026-08-01",
        ]

    return render(
        request,
        "available_dates.html",
        {"dates": dates},
    )

def instructor_list(request) :
    instructors = Instructor.objects.all()

    return render(
        request,
        "instructor_list.html",
        {"instructors":instructors},
    )
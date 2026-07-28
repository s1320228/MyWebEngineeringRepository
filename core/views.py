# Create your views here.
from datetime import date

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, ReservationForm
from .models import Instructor, Reservation


def home(request):
    return render(request, "home.html")


def object_list(request):
    return HttpResponse("Object List")


def form_page(request):
    return HttpResponse("Form Page")


def process_request(request):
    return HttpResponse("Processed")

@login_required
def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation_object = form.save(commit=False)
            reservation_object.user = request.user
            reservation_object.save()
            return redirect("my_reservations")
    else:
        form = ReservationForm(
            initial={"customer_name": request.user.username}
        )

    return render(
        request,
        "reservation.html",
        {"form": form},
    )

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
    instructor_id = request.GET.get("instructor")

    if not instructor_id:
        return render(
            request,
            "available_dates.html",
            {
                "available_dates": [],
                "message": "Select an instructor",
            },
        )

    available_dates_by_instructor = {
        1: [
            date(2026, 8, 1),
            date(2026, 8, 5),
            date(2026, 8, 10),
        ],
        2: [
            date(2026, 8, 3),
            date(2026, 8, 7),
            date(2026, 8, 12),
        ],
        3: [
            date(2026, 8, 2),
            date(2026, 8, 8),
            date(2026, 8, 15),
        ],
        4 : [
            date(2026, 7, 30),
            date(2026, 8, 2),
            date(2026, 8, 5),
            date(2026, 8, 15)
        ],
        5 : [
            date(2026, 8, 12),
            date(2026, 8, 14),
            date(2026, 8, 22),
        ],
        6 : [
            date(2026, 8, 2),
            date(2026, 8, 16),
            date(2026, 8, 22),
        ]
    }

    dates = available_dates_by_instructor.get(
        int(instructor_id),
        [],
    )

    return render(
        request,
        "available_dates.html",
        {
            "available_dates": dates,
            "message": "",
        },
    )
def instructor_list(request) :
    instructors = Instructor.objects.all()

    return render(
        request,
        "instructor_list.html",
        {"instructors":instructors},
    )

@login_required
def reservation_success(request):
    return render(request, "success.html")

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(
        user=request.user
    ).select_related("instructor")

    return render(
        request,
        "my_reservations.html",
        {"reservations": reservations},
    )

@login_required
def edit_reservation(request, reservation_id):
    reservation_object = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user,
    )

    if request.method == "POST":
        form = ReservationForm(
            request.POST,
            instance=reservation_object,
        )

        if form.is_valid():
            form.save()
            return redirect("my_reservations")

    else:
        form = ReservationForm(
            instance=reservation_object,
        )

    return render(
        request,
        "edit_reservation.html",
        {
            "form": form,
            "reservation": reservation_object,
        },
    )

@login_required
def cancel_reservation(request, reservation_id):
    reservation_object = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user,
    )

    if request.method == "POST":
        reservation_object.delete()
        return redirect("my_reservations")

    return render(
        request,
        "cancel_reservation.html",
        {"reservation": reservation_object},
    )
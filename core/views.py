# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return HttpResponse("Home Page")


def object_list(request):
    return HttpResponse("Object List")


def form_page(request):
    return HttpResponse("Form Page")


def process_request(request):
    return HttpResponse("Processed")


def go_home(request):
    return redirect("/")
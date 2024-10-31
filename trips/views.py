from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_trip(request):
    return HttpResponse("Create Trip page")

def view_trips(request):
    return HttpResponse("View Trips page")
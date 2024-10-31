from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("Signup page")

def login(request):
    return HttpResponse("Login page")
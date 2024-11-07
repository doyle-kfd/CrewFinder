from django.urls import path
from . import views

urlpatterns = [
    path('create-trip/', views.create_trip, name='create_trip'),
    path('my-trips/', views.my_trips, name='my_trips'),
]
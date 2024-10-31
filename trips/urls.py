from django.urls import path
from . import views

urlpatterns = [
    # Default URL patterns for trips
    path('create/', views.create_trip, name='create_trip'),
    path('view/', views.view_trips, name='view_trips'),
]
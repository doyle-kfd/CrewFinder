from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('apply/<int:trip_id>/', views.apply_for_trip, name='apply_for_trip'),
    path('delete_application/<int:booking_id>/', views.delete_application, name='delete_application'),
]
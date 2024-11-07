from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_trip, name='create_trip'),  # Ensure this matches the template's URL usage
    path('dashboard/', views.captain_dashboard, name='captain_dashboard'),
    path('edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),  # URL for editing a trip
]
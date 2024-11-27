from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('create/', views.create_trip, name='create_trip'),
    path('dashboard/', views.captain_dashboard, name='captain_dashboard'),  # Updated route name
    path('edit/<int:trip_id>/', views.edit_trip, name='edit_trip'),
    path('delete/<int:trip_id>/', views.delete_trip, name='delete_trip'),
]

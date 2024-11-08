from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('apply/<int:trip_id>/', views.apply_for_trip, name='apply_for_trip'),
    path('crewbooking/', include('crewbooking.urls')),
]
from django.urls import path, include
from . import views
from .views import sailing_opportunities


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sailing_opportunities/', views.sailing_opportunities, name='sailing_opportunities'),
    path('404/', views.custom_404_view, name='404'),
]

from django.urls import path, include
from . import views
from .views import sailing_opportunities
from .views import test_400_view
from .views import test_403_view
from .views import test_500_view
from .views import manual_500_view

urlpatterns = [
    # Path for the home page
    path('', views.home, name='home'),
    # Path for the about page
    path('about/', views.about, name='about'),
    # Path for the contact page
    path('contact/', views.contact, name='contact'),
    # Path for the Sailing Opportunities page
    path('sailing_opportunities/', views.sailing_opportunities,
         name='sailing_opportunities'),
    # Path for testing the 400 error
    path('test-400/', test_400_view, name='test_400'),
    # Path for testing the 403 error
    path('test-403/', test_403_view, name='test_403'),
    # Path for testing the 500 error
    path('test-500/', test_500_view, name='test_500'),
    # Path for manually triggering a 500 error page
    path('manual-500/', manual_500_view, name='manual_500'),
]

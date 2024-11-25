from django.urls import path, include
from . import views
from .views import sailing_opportunities
from .views import test_400_view
from .views import test_403_view
from .views import test_500_view
from .views import manual_500_view


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sailing_opportunities/', views.sailing_opportunities, name='sailing_opportunities'),
    path('test-400/', test_400_view, name='test_400'),
    path('test-403/', test_403_view, name='test_403'),
    path('test-500/', test_500_view, name='test_500'),
    path('manual-500/', manual_500_view, name='manual_500'),
]
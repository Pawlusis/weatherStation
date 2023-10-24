from django.urls import path
from weatherdata.views import weather_dashboard

urlpatterns = [
    path('dashboard/', weather_dashboard, name='weather_dashboard'),
]

from django.urls import path
from weatherdata.views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('temperature/', temperature_dashboard, name='temperature_dashboard'),
    path('humidity/', humidity_dashboard, name='humidity_dashboard'),
    path('air_pressure/', air_pressure_dashboard, name='air_pressure_dashboard'),
    path('wind/', wind_dashboard, name='wind_dashboard'),
    path('save_safe_values/', save_safe_values, name='save_safe_values')
]

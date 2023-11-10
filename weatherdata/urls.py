from django.urls import path
from weatherdata.views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('temperature/', temperature_dashboard, name='temperature dashboard'),
    path('humidity/', humidity_dashboard, name='humidity dashboard'),
    path('air_pressure/', air_pressure_dashboard, name='air pressure dashboard'),
    path('wind/', wind_dashboard, name= 'wind statistic dashboard')
]

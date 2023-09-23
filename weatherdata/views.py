from django.shortcuts import render
from .models import WeatherData

def show_data(request):
    weather_data = WeatherData.objects.all()
    context = {'weather_data': weather_data}
    return render(request, 'weatherdata/data.html', context)

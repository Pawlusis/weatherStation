from django.shortcuts import render
from .models import WeatherData


def show_data(request):
    weather_data = WeatherData.objects.all()
    context = {
		'weather_data': weather_data,
		'current_data': list(weather_data)[-1] if weather_data.exists() else None,
		}
    return render(request, 'weatherdata/data.html', context)

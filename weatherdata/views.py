from django.shortcuts import render
from .models import WeatherData
import json
from django.core.serializers import serialize

def temperature_dashboard(request):
    weather_data = WeatherData.objects.all()
    data = serialize('json', weather_data)
    context = {
        'weather_data': json.loads(data)
    }
    return render(request, 'weatherdata/Temperature.html', {'weather_data': json.loads(data)})

def humidity_dashboard(request):
    weather_data = WeatherData.objects.all()
    data = serialize('json', weather_data)
    context = {
        'weather_data': json.loads(data)
    }
    return render(request, 'weatherdata/Humidity.html', {'weather_data': json.loads(data)})

def air_pressure_dashboard(request):
    weather_data = WeatherData.objects.all()
    data = serialize('json', weather_data)
    context = {
        'weather_data': json.loads(data)
    }
    return render(request, 'weatherdata/air_pressure.html', {'weather_data': json.loads(data)})

def wind_dashboard(request):
    weather_data = WeatherData.objects.all()
    data = serialize('json', weather_data)
    context = {
        'weather_data': json.loads(data)
    }
    return render(request, 'weatherdata/wind.html', {'weather_data': json.loads(data)})

def menu(request):
    weather_data = WeatherData.objects.all()
    context = {
        'weather_data': weather_data,
        'current_data': list(weather_data)[-1] if weather_data.exists() else None,
    }
    return render(request, 'weatherdata/menu1.html', context)

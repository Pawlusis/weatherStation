from django.shortcuts import render, redirect
from .models import WeatherData, SafeValueRange
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
    current_data = list(weather_data)[-1] if weather_data.exists() else None

    if SafeValueRange.objects.exists():
        safe_values = SafeValueRange.objects.last()
    else:

        safe_values = SafeValueRange(
            minTemp=10.0,
            maxTemp=30.0,
            minPress=980.0,
            maxPress=1020.0,
            minWind=0.0,
            maxWind=10.0
        )

    context = {
        'weather_data': weather_data,
        'current_data': current_data,
        'safe_values': safe_values,
    }

    return render(request, 'weatherdata/menu1.html', context)

def save_safe_values(request):
    if request.method == 'POST':
        min_temp = request.POST.get('tempMin')
        max_temp = request.POST.get('tempMax')
        min_press = request.POST.get('pressMin')
        max_press = request.POST.get('pressMax')
        min_wind = request.POST.get('windMin')
        max_wind = request.POST.get('windMax')

        # Utworzenie lub aktualizacja rekordu w bazie danych
        safe_value_range, created = SafeValueRange.objects.update_or_create(
            defaults={
                'minTemp': min_temp,
                'maxTemp': max_temp,
                'minPress': min_press,
                'maxPress': max_press,
                'minWind': min_wind,
                'maxWind': max_wind
            }
        )

        return redirect('menu')  # Powrót do strony głównej

    # Obsługa innych metod niż POST
    return redirect('menu')
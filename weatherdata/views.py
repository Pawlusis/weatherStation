from django.shortcuts import render
from .models import WeatherData
import json
from django.core.serializers import serialize

def weather_dashboard(request):
    weather_data = WeatherData.objects.all()
    data = serialize('json', weather_data)
    context = {
        'weather_data': json.loads(data)
    }
    return render(request, 'weatherdata/data1.html', {'weather_data': json.loads(data)})

from django.db import models


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_pressure = models.FloatField(default=0)
    wind_speed = models.FloatField(default=0)
    wind_direction = models.CharField(max_length=2, default='N/A')
    timestamp = models.DateTimeField(auto_now_add=True)

class SafeValueRange(models.Model):
    minTemp = models.FloatField()
    maxTemp = models.FloatField()
    minPress = models.FloatField()
    maxPress = models.FloatField()
    minWind = models.FloatField()
    maxWind = models.FloatField()
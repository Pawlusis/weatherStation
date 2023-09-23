from django.db import models

class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    connection_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

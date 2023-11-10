import sys

sys.path.append('/home/pi/weatherStation/')

import os
import django
import paho.mqtt.client as mqtt
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherstation.settings')
django.setup()

from weatherdata.models import WeatherData

temperature_data = None
humidity_data = None
air_pressure_data = None
wind_speed_data = None
wind_direction_data = None


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("weather_station/temperature")
    client.subscribe("weather_station/humidity")
    client.subscribe("weather_station/air_pressure")
    client.subscribe("weather_station/wind_speed")
    client.subscribe("weather_station/wind_direction")


def on_message(client, userdata, msg):
    global temperature_data, humidity_data, air_pressure_data, wind_speed_data, wind_direction_data
    if msg.topic == "weather_station/temperature":
        temperature_data = float(msg.payload)
    elif msg.topic == "weather_station/humidity":
        humidity_data = float(msg.payload)
    elif msg.topic == "weather_station/air_pressure":
        air_pressure_data = float(msg.payload)
    elif msg.topic == "weather_station/wind_speed":
        wind_speed_data = float(msg.payload)
    elif msg.topic == "weather_station/wind_direction":
        wind_direction_data = float(msg.payload)

    if temperature_data is not None and humidity_data is not None and air_pressure_data is not None and wind_speed_data is not None and wind_direction_data is not None :
        weather_entry = WeatherData(temperature=temperature_data, humidity=humidity_data, air_pressure=air_pressure_data, wind_speed=wind_direction_data, wind_direction=wind_direction_data)
        weather_entry.save()
        temperature_data = None
        humidity_data = None
        air_pressure_data = None
        wind_speed_data = None
        wind_direction_data = None



if __name__ == "__main__":
    time.sleep(10)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    client.loop_forever()

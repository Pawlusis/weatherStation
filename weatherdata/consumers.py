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


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("weather_station/temperature")
    client.subscribe("weather_station/humidity")


def on_message(client, userdata, msg):
    global temperature_data, humidity_data
    if msg.topic == "weather_station/temperature":
        temperature_data = float(msg.payload)
    elif msg.topic == "weather_station/humidity":
        humidity_data = float(msg.payload)

    if temperature_data is not None and humidity_data is not None:
        weather_entry = WeatherData(temperature=temperature_data, humidity=humidity_data)
        weather_entry.save()
        temperature_data = None
        humidity_data = None


if __name__ == "__main__":
    time.sleep(10)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    client.loop_forever()

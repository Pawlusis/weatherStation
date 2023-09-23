import paho.mqtt.client as mqtt
from .models import WeatherData

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("weather_station")

def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8').split(',')
    temperature, humidity, connection_status = data
    WeatherData.objects.create(temperature=temperature, humidity=humidity, connection_status=connection_status)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.23", 1883, 60)
client.loop_forever()

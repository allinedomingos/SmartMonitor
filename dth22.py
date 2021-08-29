from machine import Pin
from time import sleep
import dht 
import confMqtt

sensor = dht.DHT22(Pin(14))

BROKER_IP = 'xxxxxxxxxxxx'
BROKER_PORT = 1883
CLIENT_NAME = 'Test'
BROKER_USER='xxxxxxxxxxxxxx'
BROKER_PASS='xxxxxxxxxxxxxxxxxxx'
TOPIC = 'test/dht22'

data = {'temperature': 0, 'humidity': 0}
humidity = 0;
temperature = 0;

client = confMqtt.createClient(CLIENT_NAME, BROKER_IP, BROKER_PORT, BROKER_USER, BROKER_PASS)

while True:
  try:
    if humidity is not None and temperature is not None:
      sensor.measure()
      temperature = sensor.temperature()
      humidity = sensor.humidity()
      print(u"Temperatura: {:g}\u00b0C, Umidade: {:g}%".format(temperature, humidity))
      data['temperature'] = temperature
      data['humidity'] = humidity
      confMqtt.connectBroker(client)
      confMqtt.sendPackage(client, TOPIC, data)
  except OSError as e:
      print('Erro ao tentar ler dados do sensor.')



import json
import confMqtt
import Adafruit_DHT

BROKER_IP = 'localhost'
BROKER_PORT = 1883
CLIENT_NAME = 'dth22'
BROKER_USER='hostbroken'
BROKER_PASS='passhost'
topic = 'test/dht22'

SENSOR_LIB = Adafruit_DHT.DHT22
PINO_CONF = 4
DELAY = 2

data = {'temperature': 0, 'humidity': 0}

client = confMqtt.createClient(CLIENT_NAME)
confMqtt.on_publish=confMqtt.on_publish
confMqtt.on_connect=confMqtt.on_connect
confMqtt.connect(client,BROKER_USER,BROKER_PASS,BROKER_IP)

humidity, temperature = Adafruit_DHT.read_retry(SENSOR_LIB, PINO_CONF)
    if humidity is not None and temperature is not None:
       humidity= round(humidity,2)
       temperature = round(temperature,2)
       print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
       data['temperature'] = temperature
       data['humidity'] = humidity
       package = json.dumps(data)
       confMqtt.send(client,package,TOPIC)
       print("Send..."+ package)
    else:
        print("Failed to retrieve data from humidity sensor")
   

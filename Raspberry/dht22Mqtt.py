import paho.mqtt.client as mqtt
import time

BROKER_IP = 'localhost'
BROKER_PORT = 1883
CLIENT_NAME = 'dth22'
BROKER_USER='hostbroken'
BROKER_PASS='passhost'
topic = 'test/dht22'


def on_publish(client, userdata, result):
	print('data published\n')
	pass

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

client = mqtt.Client(CLIENT_NAME)
client.on_publish = on_publish
client.on_connect = on_connect
client.username_pw_set(BROKER_USER, BROKER_PASS)
client.connect(BROKER_IP, BROKER_PORT)
client.loop_start()
client.publish('test/ttt', 'Ola')
time.sleep(10)
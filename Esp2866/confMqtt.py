from umqtt.robust import MQTTClient
from time import sleep
import machine
import ujson

def createClient(CLIENT_NAME, BROKER_IP, BROKER_PORT, BROKER_USER, BROKER_PASS):
  client = MQTTClient(CLIENT_NAME, BROKER_IP, BROKER_PORT, BROKER_USER, BROKER_PASS)
  return client
  
def connectBroker(client):
  client.connect()
  
def sendPackage(client,test_topic,data):
  package=ujson.dumps(data)
  print('Enviando dados...\n', package)
  client.publish(test_topic,package)
  sleep(10)
  

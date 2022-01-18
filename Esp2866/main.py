from umqtt.robust import MQTTClient
from time import sleep
import ujson
from machine import Pin,ADC,I2C
import onewire, ds18x20
import dht
import bh1750fvi
import confWifi
import time
import network

WiFi_SSID = "XXXXXXXXXX"
WiFi_PASS = "XXXXXXXXXX"
BROKER_IP = 'xxxxxxxxxxxx'
BROKER_PORT = 1883
CLIENT_NAME = 'Test'
BROKER_USER='xxxxxxxxxxxxxx'
BROKER_PASS='xxxxxxxxxxxxxxxxxxx'
topic_dht = "test/dht22"
topic_uv = "test/uv"
topic_lux = "test/lux"
topic_temp= "test/temp"

def connectWifi(WiFi_SSID, WiFi_PASS):
  
  wlan = network.WLAN(network.STA_IF)
  
  if not wlan.isconnected():
      print('Conectando a rede...')
      wlan.active(True)
      wlan.connect(WiFi_SSID, WiFi_PASS)
      print('Rede conectada:', wlan.ifconfig())
      print("ESP8266 pronta para enviar dados....")
      while not wlan.isconnected():
          print('Tentando conectar a rede...', WiFi_SSID)
          pass

    

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
 
  
def getUv_(pinout): 
  adc = ADC(pinout)
  adc_value = adc.read()
  voltage = (adc_value * 3.3) / 65536
  data = {'uv': 0}
   
  data['uv'] = voltage
  
  print('Pacote de dados montado:\n', data)
    
  return data
    
def getDht_(pinout):
  
  sensor = dht.DHT22(Pin(pinout))
   
  humidity = 0;
  temperature = 0;
  
  data = {'temperature': 0, 'humidity': 0}
  
  try:
    if humidity is not None and temperature is not None:
      sensor.measure()
      temperature = sensor.temperature()
      humidity = sensor.humidity()
      data['temperature'] = temperature
      data['humidity'] = humidity
      print('Pacote de dados montado:\n', data)
  except OSError as e:
      print('Erro ao tentar ler dados do sensor.')
      
  return data  
       
def getLux(pin_scl, pin_sda):
  
  data = {'luminosity': 0}

  i2c = I2C(scl=Pin(pin_scl), sda=Pin(pin_sda)) 
  ligth= bh1750fvi.sample(i2c)
  data['luminosity'] = ligth
  print('Pacote de dados montado:\n', data)
  
  return data  
  
def getTemp(pinout_temp):
  
  data = {'temperature': 0}

  ds_pin = machine.Pin(pinout_temp)
  ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
  roms = ds_sensor.scan()
  try:
    ds_sensor.convert_temp()
    #It's important to wait so the conversion can take place
    for rom in roms:
      data['temperature'] = ds_sensor.read_temp(rom)
      print('Pacote de dados montado:\n', data)
  except OSError as e:
      print('Erro ao tentar ler dados do sensor.')
   
  return data  
  
def main():
  
  pinout_dht=14
  pinout_uv=0
  pin_scl=5
  pin_sda=4
  pinout_temp=12
  
  connectWifi(WiFi_SSID, WiFi_PASS)
  
  time.sleep(100)
  
  client = createClient(CLIENT_NAME, BROKER_IP, BROKER_PORT, BROKER_USER, BROKER_PASS)
  
  while True:
    data_1 = getTemp(pinout_temp)
    data_2 = getUv_(pinout_uv)
    data_3 = getDht_(pinout_dht)
    data_4 = getLux(pin_scl,pin_sda)
   
    connectBroker(client)

    sendPackage(client,topic_temp,data_1)
    sleep(5)
    sendPackage(client,topic_uv,data_2)
    sleep(5)
    sendPackage(client,topic_dht,data_3)
    sleep(5)
    sendPackage(client,topic_lux,data_4)
    sleep(2)
    print('Novos dados serao enviados apos 5 minutos')
    time.sleep(300)
   

if __name__ == "__main__":
    main()
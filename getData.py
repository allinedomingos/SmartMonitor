from time import sleep
from machine import Pin,ADC,I2C
import onewire, ds18x20
import dht
import bh1750fvi
import confMqtt
import confWifi


BROKER_IP = 'localhost'
BROKER_PORT = 1883
CLIENT_NAME = 'Test'
BROKER_USER='xxxxxxxxxxxxxxxxxxxx'
BROKER_PASS='xxxxxxxxxxxxxxxx'
topic_dht = "test/dht22"
topic_solo = "test/uv"
topic_lux = "test/lux"
topic_temp= "test/temp"
  
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
      return -1
      
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
  #print('Found DS devices: ', roms)
  #Loops every 5 seconds forever
  try:
    ds_sensor.convert_temp()
    #It's important to wait so the conversion can take place
    time.sleep_ms(750)
    for rom in roms:
      data['temperature'] = ds_sensor.read_temp(rom)
      print('Pacote de dados montado:\n', data)
    time.sleep(5)
  except OSError as e:
      print('Erro ao tentar ler dados do sensor.')
      return -1
   
  return data  
  
def main():
  
  pinout_dht=14
  pinout_uv=0
  pin_scl=5
  pin_sda=4
  pinout_temp=12
  
  client = createClient(CLIENT_NAME, BROKER_IP, BROKER_PORT, BROKER_USER, BROKER_PASS)
  
  while True:
    data_1 = getUv_(pinout_uv)
    data_2 = getDht_(pinout_dht)
    data_3 = getLux(pin_scl,pin_sda)
    data_4 = getTemp(pinout_temp)
    connectBroker(client)
    sendPackage(client,topic_solo,data_1)
    sleep(5)
    sendPackage(client,topic_dht,data_2)
    sleep(5)
    sendPackage(client,topic_lux,data_3)
    sleep(5)
    sendPackage(client,topic_temp,data_4)
    sleep(2)
    print('Novos dados serao enviados apos 5 minutos')
    time.sleep(300)
   

if __name__ == "__main__":
    main()
  



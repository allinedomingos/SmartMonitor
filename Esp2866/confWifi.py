import network
from time import sleep
import machine
import network


WiFi_SSID = "XXXXXXXX"
WiFi_PASS = "XXXXXXXX"

wlan = network.WLAN(network.STA_IF)

def connectWifi(wlan):
  
  print('Redes encontradas...')
  print(wlan.scan())
  
  if not wlan.isconnected():
      print('Conectando a rede...')
      wlan.active(True)
      wlan.connect(WiFi_SSID, WiFi_PASS, timeout=5000)
      print('Rede conectada:', wlan.ifconfig())
      print("ESP8266 pronta para enviar dados....")
      return wlan
      while not wlan.isconnected():
          print('Tentando conectar a rede...', WiFi_SSID)
          pass
         
 
def checkConnect(wlan):
  if wlan.isconnected():
    print('Rede conectada...', wlan.ifconfig())
  else: 
    print('Conexao perdida...')
    pass
  
  

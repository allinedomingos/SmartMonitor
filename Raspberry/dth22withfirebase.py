from time import sleep
import time
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os
import Adafruit_DHT
import RPi.GPIO as GPIO

#URL firebase

URL_Firebase ='https://'

#Cria objeto firebase

firebase = firebase.FirebaseApplication(URL_Firebase, None)


#grava no datalogger

def grava_datalog(dado):

    with open('datalog.txt','a') as file:
       file.write(dado[0])
       file.write(' ')
       file.write(str(dado[1]))
       file.write(' ')
       file.write(str(dado[2]))
       file.write('\n')


#Monta informacao
def envia_info(temp,umid):
     global firebase
     data_hora = datetime.datetime.now()
     data = data_hora.strftime("%d/%m/%Y %H:%M")
     dado = data,temp,umid
     dados_firebase = {"temperatura": temp,"umidade": umid,"Data_Hora": data}
     grava_datalog(dado)
     firebase.post('/sensor',dados_firebase)
     return


def main():

    #Limpa
    GPIO.setwarnings(False)
    GPIO.cleanup()

    # Objeto sensor
    sensor = Adafruit_DHT.DHT22
    GPIO.setmode(GPIO.BOARD)


    # Define a GPIO (pino de leitura de dado)
    pino_sensor = 22

    while True:
      #  Le do sensor
	umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);

	# Se ok, mostra os valores na tela
	if umid is not None and temp is not None :
	  print ("Temp = {0:0.1f}  Umidade = {1:0.1f}").format(temp, umid);
	  envia_info(temp,umid)
	  print ("Dados enviados\n")
	else:
	# Caso erro 
	  print ("Falha ao ler dados do sensor !!!");
	time.sleep(600)

if __name__ == '__main__':

   main()

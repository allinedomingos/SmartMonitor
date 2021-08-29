#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
# Esta é nossa função de callback. Ela vai ser chamada toda vez que uma mudança for detectada no pino GPIO correspondente.
def callback(channel):
    if GPIO.input(channel):
        print('Umido')
    else:
        print('Seco')
 
 
# Set things up
channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
# Vamos cadastrar a função de callback para o nosso pino
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
 
# Loop infinito para manter o script rodando
while True:
  time.sleep(0.1)

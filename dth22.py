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
	 time.sleep(240)

if __name__ == '__main__':

   main()

import confMqtt
import json
import time

def on_log(client, userdata, level,buf):
    print("log:"+buf)

def on_connect(client, userdata, flags,rc):
    if rc==0:
       print("Conectado...")
    else:
       print("Conexão falhou..", rc) 


ip = "localhost"
topico ="/teste"

client = confMqtt.criaClient()

confMqtt.conecta(client, ip)

client.on_connect=on_connect
client.on_log=on_log

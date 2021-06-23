import paho.mqtt.client as mqtt
import time

def createClient(CLIENT_NAME):
    client = mqtt.Client(CLIENT_NAME)
    return client
    
def connect(client,BROKER_USER, BROKER_PASS, BROKER_IP,):
    client.username_pw_set(BROKER_USER, BROKER_PASS)
    client.connect(BROKER_IP)
    client.loop_start()
    print("Connected ...: ", BROKER_IP)


def on_publish(client, userdata, result):
	print('Data published\n')
	pass

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc) 

def send(client, package, topic):
    client.publish(topic, package)
    time.sleep(15)

def disconnect(client):
    client.loop_stop()
    client.disconnect()

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnect..."+str(rc))






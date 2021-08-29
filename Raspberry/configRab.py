import pika
import time

def conecta():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='dht22', durable=True)
    
    return channel

def criaFila(channel,fila):
    fila = 'dht22'
    channel.queue_declare(queue=fila, durable=True)


def envia(channel, pacote):
    channel.basic_publish(
            exchange='',
            routing_key='teste',
            body=pacote,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        
    print("Envia..." + pacote)
    print("Aguardado proxima leitura...")
    time.sleep(10)

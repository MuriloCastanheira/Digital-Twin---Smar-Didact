# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client
#from pegandosevidor import *
from Adaptador import dados
#a = str(random.randint(1,100))
#b= str(random.randint(1,100))
#zu = str([a,b])
#print(zu)
broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'tony'
password = '126673'
def atualizardados():
    time.sleep(1)
    a = dados()
    zu = str([a])
    print(zu)
    return zu

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        zu = atualizardados()
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, zu)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{zu}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

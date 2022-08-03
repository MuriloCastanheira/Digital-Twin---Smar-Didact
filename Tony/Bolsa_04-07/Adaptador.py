import serial
from opcua import Client
import random
import time

url = "opc.tcp://192.168.0.48:4840"
client = Client(url)
client.connect()
print("Client Conectado")

#############################################################################


#############################################################################
def dados():
    while True:
        time.sleep(1)
        Quant_Agua_Saida_Reservatorio = client.get_node("ns=2;i=2")
        Quant_Agua_Saida_Reservatorio = Quant_Agua_Saida_Reservatorio.get_value()
        print(Quant_Agua_Saida_Reservatorio)
        return Quant_Agua_Saida_Reservatorio
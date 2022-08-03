import serial
from opcua import Client
import random
import time

url = "opc.tcp://192.168.0.48:4840"
client = Client(url)
client.connect()
print("Client Conectado")

#############################################################################
while True:
    Quant_Agua_Saida_Reservatorio = client.get_node("ns=2;i=2")
    Quant_Agua_Saida_Reservatorio = Quant_Agua_Saida_Reservatorio.get_value()
    print(Quant_Agua_Saida_Reservatorio)

    Quant_Bomba_1_Reservatorio = client.get_node("ns=2;i=3")
    Quant_Bomba_1_Reservatorio = Quant_Bomba_1_Reservatorio.get_value()
    print(Quant_Bomba_1_Reservatorio)

    Quant_Bomba_2_Reservatorio = client.get_node("ns=2;i=4")
    Quant_Bomba_2_Reservatorio = Quant_Bomba_2_Reservatorio.get_value()
    print(Quant_Bomba_2_Reservatorio)

    Vazao_Valvula1 = client.get_node("ns=2;i=5")
    Vazao_Valvula1 = Vazao_Valvula1.get_value()
    print(Vazao_Valvula1)

    Vazao_Valvula2 = client.get_node("ns=2;i=6")
    Vazao_Valvula2 = Vazao_Valvula2.get_value()
    print(Vazao_Valvula2)

    Quant_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=7")
    Quant_Agua_Tanque_Aquecimento = Quant_Agua_Tanque_Aquecimento.get_value()
    print(Quant_Agua_Tanque_Aquecimento)

    Tempo_Processo_Tanque_Aquecimento = client.get_node("ns=2;i=8")
    Tempo_Processo_Tanque_Aquecimento = Tempo_Processo_Tanque_Aquecimento.get_value()
    print(Tempo_Processo_Tanque_Aquecimento)

    Quant_Agua_Saida_Tanque_Aquecimento = client.get_node("ns=2;i=9")
    Quant_Agua_Saida_Tanque_Aquecimento = Quant_Agua_Saida_Tanque_Aquecimento.get_value()
    print(Quant_Agua_Saida_Tanque_Aquecimento)

    Temp_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=10")
    Temp_Agua_Tanque_Aquecimento = Temp_Agua_Tanque_Aquecimento.get_value()
    print(Temp_Agua_Tanque_Aquecimento)

    Quant_Agua_Tanque_Mistura = client.get_node("ns=2;i=11")
    Quant_Agua_Tanque_Mistura = Quant_Agua_Tanque_Mistura.get_value()
    print(Quant_Agua_Tanque_Mistura)

    Quant_AguaQuente_Tanque_Mistura = client.get_node("ns=2;i=12")
    Quant_AguaQuente_Tanque_Mistura = Quant_AguaQuente_Tanque_Mistura.get_value()
    print(Quant_AguaQuente_Tanque_Mistura)

    Quant_AguaFria_Tanque_Mistura = client.get_node("ns=2;i=13")
    Quant_AguaFria_Tanque_Mistura = Quant_AguaFria_Tanque_Mistura.get_value()
    print(Quant_AguaFria_Tanque_Mistura)

    Tempo_Processo_Tanque_Mistura = client.get_node("ns=2;i=14")
    Tempo_Processo_Tanque_Mistura = Tempo_Processo_Tanque_Mistura.get_value()
    print(Tempo_Processo_Tanque_Mistura)

    Quant_Agua_Saida_Tanque_Mistura = client.get_node("ns=2;i=15")
    Quant_Agua_Saida_Tanque_Mistura = Quant_Agua_Saida_Tanque_Mistura.get_value()
    print(Quant_Agua_Saida_Tanque_Mistura)

    time.sleep(5)
#############################################################################



import serial
from opcua import Client
import random
import time

url = "opc.tcp://192.168.0.48:4840"
client = Client(url)
client.connect()
print("Client Conectado")

#############################################################################
Quant_Agua_Saida_Reservatorio = client.get_node("ns=2;i=2")
Quant_Bomba_1_Reservatorio = client.get_node("ns=2;i=3")
Quant_Bomba_2_Reservatorio = client.get_node("ns=2;i=4")
Vazao_Valvula1 = client.get_node("ns=2;i=5")
Vazao_Valvula2 = client.get_node("ns=2;i=6")
Quant_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=7")
Tempo_Processo_Tanque_Aquecimento = client.get_node("ns=2;i=8")
Quant_Agua_Saida_Tanque_Aquecimento = client.get_node("ns=2;i=9")
Temp_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=10")
Quant_Agua_Tanque_Mistura = client.get_node("ns=2;i=11")
Quant_AguaQuente_Tanque_Mistura = client.get_node("ns=2;i=12")
Quant_AguaFria_Tanque_Mistura = client.get_node("ns=2;i=13")
Tempo_Processo_Tanque_Mistura = client.get_node("ns=2;i=14")
Quant_Agua_Saida_Tanque_Mistura = client.get_node("ns=2;i=15")
#############################################################################


while True:

    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if int(a) < 20000:
        b = int(a) - 10000
        print(int(b))
        Quant_Agua_Saida_Reservatorio.set_value(int(b))

    if 30000 > int(a) > 20000:
        c = int(a) - 20000
        print(int(c))
        Quant_Bomba_1_Reservatorio.set_value(int(c))

    if 40000 > int(a) > 30000:
        d = int(a) - 30000
        print(int(d))
        Quant_Bomba_2_Reservatorio.set_value(int(d))

    if 50000 > int(a) > 40000:
        e = int(a) - 40000
        print(int(e))
        Vazao_Valvula1.set_value(int(e))

    if 60000 > int(a) > 50000:
        f = int(a) - 50000
        print(int(f))
        Vazao_Valvula2.set_value(int(f))

    if 70000 > int(a) > 60000:
        g = int(a) - 60000
        print(int(g))
        Quant_Agua_Tanque_Aquecimento.set_value(int(g))

    if 80000 > int(a) > 70000:
        h = int(a) - 70000
        print(int(h))
        Tempo_Processo_Tanque_Aquecimento.set_value(int(h))

    if 90000 > int(a) > 80000:
        i = int(a) - 80000
        print(int(i))
        Quant_Agua_Saida_Tanque_Aquecimento.set_value(int(i))

    if 100000 > int(a) > 90000:
        j = int(a) - 90000
        print(int(j))
        Temp_Agua_Tanque_Aquecimento.set_value(int(j))

    if 110000 > int(a) > 100000:
        k = int(a) - 100000
        print(int(k))
        Quant_Agua_Tanque_Mistura.set_value(int(k))

    if 120000 > int(a) > 110000:
        l = int(a) - 110000
        print(int(l))
        Quant_AguaQuente_Tanque_Mistura.set_value(int(l))

    if 130000 > int(a) > 120000:
        m = int(a) - 120000
        print(int(m))
        Quant_AguaFria_Tanque_Mistura.set_value(int(m))

    if 140000 > int(a) > 130000:
        n = int(a) - 130000
        print(int(n))
        Tempo_Processo_Tanque_Mistura.set_value(int(n))

    if 150000 > int(a) > 140000:
        o = int(a) - 140000
        print(int(o))
        Quant_Agua_Saida_Tanque_Mistura.set_value(int(o))

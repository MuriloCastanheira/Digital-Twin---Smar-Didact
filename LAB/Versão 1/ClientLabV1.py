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
	Quant_Agua_Saida_Reservatorio.set_value(int(random.uniform(0, 10)))
	Quant_Bomba_1_Reservatorio.set_value(int(random.uniform(0, 500)))
	Quant_Bomba_2_Reservatorio.set_value(int(random.uniform(0, 500)))
	Vazao_Valvula1.set_value(int(random.uniform(0, 10)))
	Vazao_Valvula2.set_value(int(random.uniform(0, 10)))
	Quant_Agua_Tanque_Aquecimento.set_value(int(random.uniform(0, 1000)))
	Tempo_Processo_Tanque_Aquecimento.set_value(int(random.uniform(0, 60)))
	Quant_Agua_Saida_Tanque_Aquecimento.set_value(int(random.uniform(0, 60)))
	Temp_Agua_Tanque_Aquecimento.set_value(int(random.uniform(0, 100)))
	Quant_Agua_Tanque_Mistura.set_value(int(random.uniform(0, 1000)))
	Quant_AguaQuente_Tanque_Mistura.set_value(int(random.uniform(0, 500)))
	Quant_AguaFria_Tanque_Mistura.set_value(int(random.uniform(0, 500)))
	Tempo_Processo_Tanque_Mistura.set_value(int(random.uniform(0, 60)))
	Quant_Agua_Saida_Tanque_Mistura.set_value(int(random.uniform(0, 60)))
	time.sleep(5)

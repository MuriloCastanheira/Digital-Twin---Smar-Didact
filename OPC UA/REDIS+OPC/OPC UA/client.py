from opcua import Client
import time
import random

url = "opc.tcp://192.168.0.21:4840"

client = Client(url)

client.connect()
print("Client Connected")

Temp_1 = client.get_node("ns=2;i=2")
Temp_2 = client.get_node("ns=2;i=3")
Temp_3 = client.get_node("ns=2;i=4")
Temp_4 = client.get_node("ns=2;i=5")

while True:
	Temp_1.set_value(int(random.uniform(0, 300)))
	Temp_2.set_value(int(random.uniform(30, 100)))
	Temp_3.set_value(float(random.uniform(5, -30)))
	Temp_4.set_value(int(random.uniform(20, 25)))
	t1 = Temp_1.get_value()
	t2 = Temp_2.get_value()
	t3 = Temp_3.get_value()
	t4 = Temp_4.get_value()
	print("Fornalha: " ,t1,"Forma: ",t2,"Congelador: ", t3,"Sala: ",t4)
	time.sleep(1)



from opcua import Server
import serial
from serial import Serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)

server = Server()
url = "opc.tcp://192.168.0.18:4840"
server.set_endpoint(url)

node = server.get_objects_node()

name="OPC_TEST_server"
addspace = server.register_namespace(name)

sensores = node.add_object("ns=2;s=Sensores", "sensores")
Potenciometro = sensores.add_variable("ns=2;s=Potenciometro", "Potenciometro", 0)


Potenciometro.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
	data = ser.readline(1000)
	a = int(data)
	Potenciometro.set_value(a)

	print(Potenciometro.get_value())

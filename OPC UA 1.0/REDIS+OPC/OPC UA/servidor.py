from opcua import Client
from pyModbusTCP.server import DataBank, ModbusServer
import random
import time

url = "opc.tcp://192.168.0.21:4840"

client = Client(url)

client.connect()
print("Client Connected")

Temp_1 = client.get_node("ns=2;i=2")
Temp_2 = client.get_node("ns=2;i=3")
Temp_3 = client.get_node("ns=2;i=4")
Temp_4 = client.get_node("ns=2;i=5")

class ServidorMODBUS():
	"""
	Classe Servidor Modbus
	"""

	def __init__(self, host_ip, port):
		"""
		Construtor
		"""
		self._server = ModbusServer(host = host_ip,port=port,no_block= True)
		self._db = DataBank

	def run(self):
		"""
		Execução do servidor Modbus
		"""
		try:
			self._server.start()
			print("Servidor MODBUS em execução")
			while True:
				t1 = Temp_1.get_value()
				t2 = Temp_2.get_value()
				t3 = Temp_3.get_value()
				t4 = Temp_4.get_value()
				self._db.set_words(1,[t1])
				self._db.set_words(2,[t2])
				self._db.set_words(3,[t3])
				self._db.set_words(4,[t4])
			
				
				
				
				time.sleep(1)
		except Exception as e:
			print("Erro: ",e.args)

                

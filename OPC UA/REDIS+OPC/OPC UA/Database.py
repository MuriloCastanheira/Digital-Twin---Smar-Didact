from opcua import Client
import time
import redis
import redis
import json

url = "opc.tcp://192.168.0.21:4840"
r = redis.Redis(host="localhost", port=6379, db=0, password="")

client = Client(url)

client.connect()
print("Client Connected")

Temp_1 = client.get_node("ns=2;i=2")
Temp_2 = client.get_node("ns=2;i=3")
Temp_3 = client.get_node("ns=2;i=4")
Temp_4 = client.get_node("ns=2;i=5")

fornalha = Temp_1.get_value()
forma = Temp_1.get_value()
congelador = Temp_1.get_value()
sala = Temp_1.get_value()
nome = "Teste de Banco de Dados"
t = time.localtime()

while(True):
  output = {
  	"Nome": nome,
  	"Ano": t[0],
  	"Mes": t[1],
  	"Dia": t[2],
  	"Hora": t[3],
  	"Minutos": t[4],
  	"Segundos": t[5],
    "Fornalha": int(fornalha),
    "Forma": int(forma),
    "Congelador": int(congelador),
    "Sala": int(sala),
    
  }
  print(output)
  print(r.pfadd("Sensores",1000, output))
  time.sleep(5)

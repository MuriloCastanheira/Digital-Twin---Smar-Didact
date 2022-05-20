from opcua import Client
import time

url = "opc.tcp://127.1.0.1:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
    param = client.get_node("ns=2;i=2")
    parametro = param.get_value()
    print(parametro)

    time.sleep(1)

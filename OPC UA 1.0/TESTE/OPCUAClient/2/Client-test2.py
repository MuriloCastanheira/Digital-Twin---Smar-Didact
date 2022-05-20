from opcua import Client


url = "opc.tcp://0.0.0.0:4840"
client = Client(url)

client.connect()

var = client.get_node("ns=2;i=3")
print("Client Connected")
x = input("subiu?")
var.set_value(x)
from opcua import Client


url = "opc.https://localshost:4840"
client = Client(url)

client.connect()

var = client.get_node("ns=2;i=2")
print("Client Connected")

var.set_value("1")
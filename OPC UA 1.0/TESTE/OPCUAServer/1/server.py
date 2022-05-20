from opcua import Server
from random import randint
import time

server = Server()

url = "opc.tcp://127.1.0.1:4840"

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

SNN = Param.add_variable(addspace, "SUAVE NA NAVE",0)

SNN.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    SNNa = "A DONA ARANHA SUBIU PELA PAREDE"

    print(SNNa)

    SNN.set_value(SNNa)
    
    time.sleep(1)
    SNNa = "PELA PAREDE"

    print(SNNa)

    SNN.set_value(SNNa)
    
    time.sleep(1)
    
    

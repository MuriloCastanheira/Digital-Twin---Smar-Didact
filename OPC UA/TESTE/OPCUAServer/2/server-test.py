from opcua import Server
import time


server = Server()
url = "opc.tcp://0.0.0.0:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")
Sensores = node.add_object(addspace, "Sensores")

dona = Param.add_variable(addspace, "Dona Aranha",0)
parede = Param.add_variable(addspace, "Parade",0)
infravermelho = Sensores.add_object(addspace, "Infravermelho")
Infra = infravermelho.add_variable(addspace, "Infravermelho",10)
dona.set_writable()
parede.set_writable()

server.start()
print("Server started at {}".format(url))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

donaaranha = "A DONA ARANHA SUBIU PELA PAREDE"
par = "?"
print(donaaranha)
dona.set_value(donaaranha)
dona.set_value(donaaranha)
parede.set_value(par)


while True:
    
    print("Subiu?")
    print(parede.get_value())	
    
    
    time.sleep(1)
    
    

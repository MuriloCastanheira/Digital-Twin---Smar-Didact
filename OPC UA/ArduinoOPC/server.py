from opcua import Server
import time

server = Server()
url = "opc.tcp://192.168.0.18:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")

ventilador = Param.add_variable(addspace, "Ventilador",0)

ventilador.set_writable()

server.start()
print("Server started at {}".format(url))

porcentagem = 0
ventilador.set_value(porcentagem)


while True:
    
    print("% ")
    print(ventilador.get_value())	
    
    
    time.sleep(1)


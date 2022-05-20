from opcua import Server
import time

server = Server()
url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

name = "OPCUA SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")

var = Param.add_variable(addspace, "Variable",10)
var.set_writable()

server.start()

print("Server started at {}".format(url))

while True:
    
    t = var.get_value()	
    print("Value is {}".format(t))
    
    time.sleep(1)
    
    

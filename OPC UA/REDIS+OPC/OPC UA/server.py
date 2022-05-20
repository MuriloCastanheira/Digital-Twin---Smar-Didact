from opcua import Server

server = Server()
url = "opc.tcp://192.168.0.21:4840"
server.set_endpoint(url)

node = server.get_objects_node()

name="OPC_TEST_server"
addspace = server.register_namespace(name)

sensores = node.add_object(addspace, "sensores")
Temperatura_Fornalha = sensores.add_variable(addspace, "Temp_1", int(0))
Temperatura_Forma = sensores.add_variable(addspace, "Temp_2", int(0))
Temperatura_Congelador = sensores.add_variable(addspace, "Temp_3", float(0))
Temperatura_Sala = sensores.add_variable(addspace, "Temp_4", int(0))

Temperatura_Fornalha.set_writable()
Temperatura_Forma.set_writable()
Temperatura_Congelador.set_writable()
Temperatura_Sala.set_writable()

server.start()
print("Server started at {}".format(url))

from opcua import Server

server = Server()
url = "opc.tcp://192.168.0.48:4840"
server.set_endpoint(url)

node = server.get_objects_node()

name = "Server Lab"
addspace = server.register_namespace(name)


############### Paremetros #########################################################################################
Paremetros = node.add_object(addspace, "Parametros")

Quant_Agua_Saida_Reservatorio = Paremetros.add_variable(addspace,"Quant_Agua_Saida_Reservatorio",int(0))
############### Bombas #############################################################################################
Quant_Bomba_1_Reservatorio = Paremetros.add_variable(addspace,"Quant_Bomba_1_Reservatorio",int(0))
Quant_Bomba_2_Reservatorio = Paremetros.add_variable(addspace,"Quant_Bomba_2_Reservatorio",int(0))
############### Valvulas ###########################################################################################
Vazao_Valvula1 = Paremetros.add_variable(addspace,"Vazao_Valvula1",int(0))
Vazao_Valvula2 = Paremetros.add_variable(addspace,"Vazao_Valvula2",int(0))
################## TANQUE DE AQUECIMENTO ###########################################################################
Quant_Agua_Tanque_Aquecimento = Paremetros.add_variable(addspace,"Quant_Agua_Tanque_Aquecimento",int(0))
Tempo_Processo_Tanque_Aquecimento = Paremetros.add_variable(addspace,"Tempo_Processo_Tanque_Aquecimento",int(0))
Quant_Agua_Saida_Tanque_Aquecimento = Paremetros.add_variable(addspace,"Quant_Agua_Saida_Tanque_Aquecimento",int(0))
Temp_Agua_Tanque_Aquecimento = Paremetros.add_variable(addspace,"Temp_Agua_Tanque_Aquecimento",int(0))
################## TANQUE DE MISTURA ###############################################################################
Quant_Agua_Tanque_Mistura = Paremetros.add_variable(addspace,"Quant_Agua_Tanque_Mistura",int(0))
Quant_AguaQuente_Tanque_Mistura = Paremetros.add_variable(addspace,"Quant_AguaQuente_Tanque_Mistura",int(0))
Quant_AguaFria_Tanque_Mistura = Paremetros.add_variable(addspace,"Quant_AguaFria_Tanque_Mistura",int(0))
Tempo_Processo_Tanque_Mistura = Paremetros.add_variable(addspace,"Tempo_Processo_Tanque_Mistura",int(0))
Quant_Agua_Saida_Tanque_Mistura = Paremetros.add_variable(addspace,"Quant_Agua_Saida_Tanque_Mistura",int(0))

####################################################################################################################
Quant_Agua_Saida_Reservatorio.set_writable()
Quant_Bomba_1_Reservatorio.set_writable()
Quant_Bomba_2_Reservatorio.set_writable()
Vazao_Valvula1.set_writable()
Vazao_Valvula2.set_writable()
Quant_Agua_Tanque_Aquecimento.set_writable()
Tempo_Processo_Tanque_Aquecimento.set_writable()
Quant_Agua_Saida_Tanque_Aquecimento.set_writable()
Temp_Agua_Tanque_Aquecimento.set_writable()
Quant_Agua_Tanque_Mistura.set_writable()
Quant_AguaQuente_Tanque_Mistura.set_writable()
Quant_AguaFria_Tanque_Mistura.set_writable()
Tempo_Processo_Tanque_Mistura.set_writable()
Quant_Agua_Saida_Tanque_Mistura.set_writable()
#####################################################################################################################

server.start()
print("Server started at {}".format(url))
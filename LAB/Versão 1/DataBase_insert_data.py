import mysql.connector
from mysql.connector import Error
from opcua import Client
import time

url = "opc.tcp://192.168.0.48:4840"
client = Client(url)
client.connect()
print("Client Conectado")

###################################################################################

Quant_Agua_Saida_Reservatorio = client.get_node("ns=2;i=2")
Quant_Bomba_1_Reservatorio = client.get_node("ns=2;i=3")
Quant_Bomba_2_Reservatorio = client.get_node("ns=2;i=4")
Vazao_Valvula1 = client.get_node("ns=2;i=5")
Vazao_Valvula2 = client.get_node("ns=2;i=6")
Quant_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=7")
Tempo_Processo_Tanque_Aquecimento = client.get_node("ns=2;i=8")
Quant_Agua_Saida_Tanque_Aquecimento = client.get_node("ns=2;i=9")
Temp_Agua_Tanque_Aquecimento = client.get_node("ns=2;i=10")
Quant_Agua_Tanque_Mistura = client.get_node("ns=2;i=11")
Quant_AguaQuente_Tanque_Mistura = client.get_node("ns=2;i=12")
Quant_AguaFria_Tanque_Mistura = client.get_node("ns=2;i=13")
Tempo_Processo_Tanque_Mistura = client.get_node("ns=2;i=14")
Quant_Agua_Saida_Tanque_Mistura = client.get_node("ns=2;i=15")
ID = 1

####################################################################################
while True:
        ID = ID + 1
        dados = ID, Quant_Agua_Saida_Reservatorio.get_value(), Quant_Bomba_1_Reservatorio.get_value(), Quant_Bomba_2_Reservatorio.get_value(), Vazao_Valvula1.get_value(), Vazao_Valvula2.get_value(), Quant_Agua_Tanque_Aquecimento.get_value(), Tempo_Processo_Tanque_Aquecimento.get_value(), Quant_Agua_Saida_Tanque_Aquecimento.get_value(), Temp_Agua_Tanque_Aquecimento.get_value(), Quant_Agua_Tanque_Mistura.get_value(), Quant_AguaQuente_Tanque_Mistura.get_value(), Quant_AguaFria_Tanque_Mistura.get_value(), Tempo_Processo_Tanque_Mistura.get_value(), Quant_Agua_Saida_Tanque_Mistura.get_value() 
        declaração = """INSERT INTO dados VALUES """

        sql = str(declaração) + str(dados) 
        try:
                con = mysql.connector.connect(host = 'localhost',database = 'dados',user = 'root',passwd = '')
                inserir_dados = sql

                cursor = con.cursor()
                cursor.execute(inserir_dados)
                con.commit()
                print(cursor.rowcount, "Registros inseridos na tabela!")
                cursor.close()
        except Error as erro:
                print("Falha ao inserir dados no MySQL: ()".format(erro))
        finally:
                if (con.is_connected()):
                        con.close()
                        print("Conexão ao MySQL finalizada")
        time.sleep(5)

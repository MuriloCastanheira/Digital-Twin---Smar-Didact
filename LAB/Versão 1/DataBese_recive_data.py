##video de exemplo https://youtu.be/GheUY9b_-ww
import mysql.connector
from mysql.connector import Error
import pandas as pd

excel = pd.read_excel("D:\Documentos\Bolsa\LAB\Versão 1\Dados.xlsx")

########################################################################################################################
Quant_Agua_Saida_Reservatorio = [10000, 0, 0]
Quant_Bomba_1_Reservatorio = [10000, 0, 0]
Quant_Bomba_2_Reservatorio = [10000, 0, 0]
Vazao_Valvula1 = [10000, 0, 0]
Vazao_Valvula2 = [10000, 0, 0]
Quant_Agua_Tanque_Aquecimento = [10000, 0, 0]
Tempo_Processo_Tanque_Aquecimento = [10000, 0, 0]
Quant_Agua_Saida_Tanque_Aquecimento = [10000, 0, 0]
Temp_Agua_Tanque_Aquecimento = [10000, 0, 0]
Quant_Agua_Tanque_Mistura = [10000, 0, 0]
Quant_AguaQuente_Tanque_Mistura = [10000, 0, 0]
Quant_AguaFria_Tanque_Mistura = [10000, 0, 0]
Tempo_Processo_Tanque_Mistura = [10000, 0, 0]
Quant_Agua_Saida_Tanque_Mistura = [10000, 0, 0]
########################################################################################################################
try:
    con = mysql.connector.connect(host='localhost', database='labv1', user='root', passwd='')

    consulta_sql = "select * from dados"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    total = cursor.rowcount

    for linha in linhas:
########################################################################################################################
        Quant_Agua_Saida_Reservatorio[1] += linha[1]
        if Quant_Agua_Saida_Reservatorio[0] > linha[1]:
            Quant_Agua_Saida_Reservatorio[0] = linha[1]
        if Quant_Agua_Saida_Reservatorio[2] < linha[1]:
            Quant_Agua_Saida_Reservatorio[2] = linha[1]
########################################################################################################################
        Quant_Bomba_1_Reservatorio[1] += linha[2]
        if Quant_Bomba_1_Reservatorio[0] > linha[2]:
            Quant_Bomba_1_Reservatorio[0] = linha[2]
        if Quant_Bomba_1_Reservatorio[2] < linha[2]:
            Quant_Bomba_1_Reservatorio[2] = linha[2]
########################################################################################################################
        Quant_Bomba_2_Reservatorio[1] += linha[3]
        if Quant_Bomba_2_Reservatorio[0] > linha[3]:
            Quant_Bomba_2_Reservatorio[0] = linha[3]
        if Quant_Bomba_2_Reservatorio[2] < linha[3]:
            Quant_Bomba_2_Reservatorio[2] = linha[3]
########################################################################################################################
        Vazao_Valvula1[1] += linha[4]
        if Vazao_Valvula1[0] > linha[4]:
            Vazao_Valvula1[0] = linha[4]
        if Vazao_Valvula1[2] < linha[4]:
            Vazao_Valvula1[2] = linha[4]
########################################################################################################################
            Vazao_Valvula2[1] += linha[5]
            if Vazao_Valvula2[0] > linha[5]:
                Vazao_Valvula2[0] = linha[5]
            if Vazao_Valvula2[2] < linha[5]:
                Vazao_Valvula2[2] = linha[5]
########################################################################################################################
        Quant_Agua_Tanque_Aquecimento[1] += linha[6]
        if Quant_Agua_Tanque_Aquecimento[0] > linha[6]:
            Quant_Agua_Tanque_Aquecimento[0] = linha[6]
        if Quant_Agua_Tanque_Aquecimento[2] < linha[6]:
            Quant_Agua_Tanque_Aquecimento[2] = linha[6]
########################################################################################################################
        Tempo_Processo_Tanque_Aquecimento[1] += linha[7]
        if Tempo_Processo_Tanque_Aquecimento[0] > linha[7]:
            Tempo_Processo_Tanque_Aquecimento[0] = linha[7]
        if Tempo_Processo_Tanque_Aquecimento[2] < linha[7]:
            Tempo_Processo_Tanque_Aquecimento[2] = linha[7]
########################################################################################################################
        Quant_Agua_Saida_Tanque_Aquecimento[1] += linha[8]
        if Quant_Agua_Saida_Tanque_Aquecimento[0] > linha[8]:
            Quant_Agua_Saida_Tanque_Aquecimento[0] = linha[8]
        if Quant_Agua_Saida_Tanque_Aquecimento[2] < linha[8]:
            Quant_Agua_Saida_Tanque_Aquecimento[2] = linha[8]
########################################################################################################################
        Temp_Agua_Tanque_Aquecimento[1] += linha[9]
        if Temp_Agua_Tanque_Aquecimento[0] > linha[9]:
            Temp_Agua_Tanque_Aquecimento[0] = linha[9]
        if Temp_Agua_Tanque_Aquecimento[2] < linha[9]:
            Temp_Agua_Tanque_Aquecimento[2] = linha[9]
########################################################################################################################
        Quant_Agua_Tanque_Mistura[1] += linha[10]
        if Quant_Agua_Tanque_Mistura[0] > linha[10]:
            Quant_Agua_Tanque_Mistura[0] = linha[10]
        if Quant_Agua_Tanque_Mistura[2] < linha[10]:
            Quant_Agua_Tanque_Mistura[2] = linha[10]
########################################################################################################################
        Quant_AguaQuente_Tanque_Mistura[1] += linha[11]
        if Quant_AguaQuente_Tanque_Mistura[0] > linha[11]:
            Quant_AguaQuente_Tanque_Mistura[0] = linha[11]
        if Quant_AguaQuente_Tanque_Mistura[2] < linha[11]:
            Quant_AguaQuente_Tanque_Mistura[2] = linha[11]
########################################################################################################################
        Quant_AguaFria_Tanque_Mistura[1] += linha[12]
        if Quant_AguaFria_Tanque_Mistura[0] > linha[12]:
            Quant_AguaFria_Tanque_Mistura[0] = linha[12]
        if Quant_AguaFria_Tanque_Mistura[2] < linha[12]:
            Quant_AguaFria_Tanque_Mistura[2] = linha[12]
########################################################################################################################
        Tempo_Processo_Tanque_Mistura[1] += linha[13]
        if Tempo_Processo_Tanque_Mistura[0] > linha[13]:
            Tempo_Processo_Tanque_Mistura[0] = linha[13]
        if Tempo_Processo_Tanque_Mistura[2] < linha[13]:
            Tempo_Processo_Tanque_Mistura[2] = linha[13]
########################################################################################################################
        Quant_Agua_Saida_Tanque_Mistura[1] += linha[14]
        if Quant_Agua_Saida_Tanque_Mistura[0] > linha[14]:
            Quant_Agua_Saida_Tanque_Mistura[0] = linha[14]
        if Quant_Agua_Saida_Tanque_Mistura[2] < linha[14]:
            Quant_Agua_Saida_Tanque_Mistura[2] = linha[14]
########################################################################################################################

except Error as e:
    print("Error ao acessar tabela MySQL")
finally:
    if con.is_connected():
        con.close()
        cursor.close()
        print("Conexão encerrada")

Quant_Agua_Saida_Reservatorio[1] = Quant_Agua_Saida_Reservatorio[1] / total
Quant_Bomba_1_Reservatorio[1] = Quant_Bomba_1_Reservatorio[1] / total
Quant_Bomba_2_Reservatorio[1] = Quant_Bomba_2_Reservatorio[1] / total
Vazao_Valvula1[1] = Vazao_Valvula1[1] / total
Vazao_Valvula2[1] = Vazao_Valvula2[1] / total
Quant_Agua_Tanque_Aquecimento[1] = Quant_Agua_Tanque_Aquecimento[1] / total
Tempo_Processo_Tanque_Aquecimento[1] = Tempo_Processo_Tanque_Aquecimento[1] / total
Quant_Agua_Saida_Tanque_Aquecimento[1] = Quant_Agua_Saida_Tanque_Aquecimento[1] / total
Temp_Agua_Tanque_Aquecimento[1] = Temp_Agua_Tanque_Aquecimento[1] / total
Quant_Agua_Tanque_Mistura[1] = Quant_Agua_Tanque_Mistura[1] / total
Quant_AguaQuente_Tanque_Mistura[1] = Quant_AguaQuente_Tanque_Mistura[1] / total
Quant_AguaFria_Tanque_Mistura[1] = Quant_AguaFria_Tanque_Mistura[1] / total
Tempo_Processo_Tanque_Mistura[1] = Tempo_Processo_Tanque_Mistura[1] / total
Quant_Agua_Saida_Tanque_Mistura[1] = Quant_Agua_Saida_Tanque_Mistura[1] / total

########################################################################################################################

print(Quant_Agua_Saida_Reservatorio)
print(Quant_Bomba_1_Reservatorio)
print(Quant_Bomba_2_Reservatorio)
print(Vazao_Valvula1)
print(Vazao_Valvula2)
print(Quant_Agua_Tanque_Aquecimento)
print(Tempo_Processo_Tanque_Aquecimento)
print(Quant_Agua_Saida_Tanque_Aquecimento)
print(Temp_Agua_Tanque_Aquecimento)
print(Quant_Agua_Tanque_Mistura)
print(Quant_AguaQuente_Tanque_Mistura)
print(Quant_AguaFria_Tanque_Mistura)
print(Tempo_Processo_Tanque_Mistura)
print(Quant_Agua_Saida_Tanque_Mistura)


excel["1"] =  Quant_Agua_Saida_Reservatorio
excel["2"] =  Quant_Bomba_1_Reservatorio
excel["3"] =  Quant_Bomba_2_Reservatorio
excel["4"] =  Vazao_Valvula1
excel["5"] =  Vazao_Valvula2
excel["6"] =  Quant_Agua_Tanque_Aquecimento
excel["7"] =  Tempo_Processo_Tanque_Aquecimento
excel["8"] =  Quant_Agua_Saida_Tanque_Aquecimento
excel["9"] =  Temp_Agua_Tanque_Aquecimento
excel["10"] =  Quant_Agua_Tanque_Mistura
excel["11"] =  Quant_AguaQuente_Tanque_Mistura
excel["12"] =  Quant_AguaFria_Tanque_Mistura
excel["13"] =  Tempo_Processo_Tanque_Mistura
excel["14"] =  Quant_Agua_Saida_Tanque_Mistura
print(excel)
excel.to_excel("Dados.xlsx")

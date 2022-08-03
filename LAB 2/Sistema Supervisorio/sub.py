# python3.6
import random
from paho.mqtt import client as mqtt_client
import xlsxwriter
import pandas as pd

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'tony'
password = '126673'


def data_treatment(data):
    # Pega a resposta do mqtt e adapta em uma lista
    new_data = ""
    tamanho = len(data)
    contador_data = 0
    contador_new_data = 0
    while contador_data < tamanho:
        if data[contador_data] == '[' or data[contador_data] == ']' or data[contador_data] == ',':
            contador_data += 1
        else:
            new_data = new_data + data[contador_data]
            contador_data += 1
            contador_new_data += 1
    new_data = new_data.split()
    return new_data


def ler_excel():
    df = pd.read_excel("data.xlsx")
    data_min = [df['a'][0], df['b'][0], df['c'][0], df['d'][0], df['e'][0], df['f'][0], df['g'][0], df['h'][0],
                df['i'][0], df['j'][0], df['k'][0], df['l'][0], df['m'][0], df['n'][0]]
    data_med = [df['a'][1], df['b'][1], df['c'][1], df['d'][1], df['e'][1], df['f'][1], df['g'][1], df['h'][1],
                df['i'][1], df['j'][1], df['k'][1], df['l'][1], df['m'][1], df['n'][1]]
    data_max = [df['a'][2], df['b'][2], df['c'][2], df['d'][2], df['e'][2], df['f'][2], df['g'][2], df['h'][2],
                df['i'][2], df['j'][2], df['k'][2], df['l'][2], df['m'][2], df['n'][2]]
    data_soma = [df['a'][3], df['b'][3], df['c'][3], df['d'][3], df['e'][3], df['f'][3], df['g'][3], df['h'][3],
                 df['i'][3], df['j'][3], df['k'][3], df['l'][3], df['m'][3], df['n'][3]]
    data_n = df['a'][4]
    data = [data_min, data_med, data_max, data_soma, data_n]
    return data


def data_excel(data):
    # O que eu tenho que fazer?
    # Ler das linhas do Excel que corresponde aos valores min. méd e max
    # E coloca-los nas listas que estão vazias
    # talvez separar isso em uma função seja uma abordagem melhor
    data = data_treatment(data)
    data_tri = ler_excel()
    data_min = data_tri[0]
    data_med = data_tri[1]
    data_max = data_tri[2]
    data_som = data_tri[3]
    data_n = data_tri[4]

    a = 0
    print(data_som, data_n)
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()
    # depois fazer relacionar com os dados mais recentes
    # print("UM")
    worksheet.write('A1', "CLASS")
    worksheet.write('B1', "a")
    worksheet.write('C1', "b")
    worksheet.write('D1', "c")
    worksheet.write('E1', "d")
    worksheet.write('F1', "e")
    worksheet.write('G1', "f")
    worksheet.write('H1', "g")
    worksheet.write('I1', "h")
    worksheet.write('J1', "i")
    worksheet.write('K1', "j")
    worksheet.write('L1', "k")
    worksheet.write('M1', "l")
    worksheet.write('N1', "m")
    worksheet.write('O1', "n")
    # print("DOIS")

    ############MEDIANA##############################
    n = int(data_n) + 1
    worksheet.write('A6', "n")
    worksheet.write('B6', n)
    if data_med[0] == 0 and data_med[1] == 0:

        data_med = data
        data_som = data
    else:
        while a < len(data):
            data_som[a] = (int(data_som[a]) + int(data[a]))
            a += 1
    worksheet.write('A5', "soma")
    worksheet.write('B5', data_som[0])
    worksheet.write('C5', data_som[1])
    worksheet.write('D5', data_som[2])
    worksheet.write('E5', data_som[3])
    worksheet.write('F5', data_som[4])
    worksheet.write('G5', data_som[5])
    worksheet.write('H5', data_som[6])
    worksheet.write('I5', data_som[7])
    worksheet.write('J5', data_som[8])
    worksheet.write('K5', data_som[9])
    worksheet.write('L5', data_som[10])
    worksheet.write('M5', data_som[11])
    worksheet.write('N5', data_som[12])
    worksheet.write('O5', data_som[13])

    worksheet.write('A3', "MED")
    worksheet.write('B3', (int(data_som[0])) / n)
    worksheet.write('C3', (int(data_som[1])) / n)
    worksheet.write('D3', (int(data_som[2])) / n)
    worksheet.write('E3', (int(data_som[3])) / n)
    worksheet.write('F3', (int(data_som[4])) / n)
    worksheet.write('G3', (int(data_som[5])) / n)
    worksheet.write('H3', (int(data_som[6])) / n)
    worksheet.write('I3', (int(data_som[7])) / n)
    worksheet.write('J3', (int(data_som[8])) / n)
    worksheet.write('K3', (int(data_som[9])) / n)
    worksheet.write('L3', (int(data_som[10])) / n)
    worksheet.write('M3', (int(data_som[11])) / n)
    worksheet.write('N3', (int(data_som[12])) / n)
    worksheet.write('O3', (int(data_som[13])) / n)
    # print(data_med)
    # print("TRES")

    ######MIN###################################
    mini = 0
    while mini < len(data):

        if int(data[mini]) < int(data_min[mini]):
            data_min[mini] = data[mini]
        mini += 1

    worksheet.write('A2', "MIN")
    worksheet.write('B3', data_med[0])
    worksheet.write('B2', data_min[0])
    worksheet.write('C2', data_min[1])
    worksheet.write('D2', data_min[2])
    worksheet.write('E2', data_min[3])
    worksheet.write('F2', data_min[4])
    worksheet.write('G2', data_min[5])
    worksheet.write('H2', data_min[6])
    worksheet.write('I2', data_min[7])
    worksheet.write('J2', data_min[8])
    worksheet.write('K2', data_min[9])
    worksheet.write('L2', data_min[10])
    worksheet.write('M2', data_min[11])
    worksheet.write('N2', data_min[12])
    worksheet.write('O2', data_min[13])

    # print(data_min)
    #  print("QUATRO")
    ######MIN###################################
    maxi = 0
    while maxi < len(data):
        if int(data[maxi]) > int(data_max[maxi]):
            data_max[maxi] = data[maxi]
        maxi += 1

    worksheet.write('A4', "MAX")
    worksheet.write('B4', data_max[0])
    worksheet.write('C4', data_max[1])
    worksheet.write('D4', data_max[2])
    worksheet.write('E4', data_max[3])
    worksheet.write('F4', data_max[4])
    worksheet.write('G4', data_max[5])
    worksheet.write('H4', data_max[6])
    worksheet.write('I4', data_max[7])
    worksheet.write('J4', data_max[8])
    worksheet.write('K4', data_max[9])
    worksheet.write('L4', data_max[10])
    worksheet.write('M4', data_max[11])
    worksheet.write('N4', data_max[12])
    worksheet.write('O4', data_max[13])
    workbook.close()
    print("SALVO")
    # print("CINCO")

    # print(data_max)


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, zu):
        data_excel(zu.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

import random
import time
import serial
# gerar dados falso

Quant_Agua_Reservatorio = 0
Quant_Bomba_1_Reservatorio = 0
Quant_Bomba_2_Reservatorio = 0
Vazao_Valvula1 = 0
Vazao_Valvula2 = 0
Quant_Agua_Tanque_Aquecimento = 0
Tempo_Processo_Tanque_Aquecimento = 0
Quant_Agua_Saida_Tanque_Aquecimento = 0
Temp_Agua_Tanque_Aquecimento = 0
Quant_Agua_Tanque_Mistura = 0
Quant_AguaQuente_Tanque_Mistura = 0
Quant_AguaFria_Tanque_Mistura = 0
Tempo_Processo_Tanque_Mistura = 0
Quant_Agua_Saida_Tanque_Mistura = 0

while True:
    Quant_Agua_Saida_Reservatorio = int(random.uniform(0, 1000))

    Quant_Bomba_1_Reservatorio = int(random.uniform(0, 500))

    Quant_Bomba_2_Reservatorio = int(random.uniform(0, 500))

    Vazao_Valvula1 = int(random.uniform(0, 10))

    Vazao_Valvula2 = int(random.uniform(0, 10))

    Quant_Agua_Tanque_Aquecimento = int(random.uniform(0, 1000))

    Tempo_Processo_Tanque_Aquecimento = int(random.uniform(0, 60))

    Quant_Agua_Saida_Tanque_Aquecimento = int(random.uniform(0, 60))

    Temp_Agua_Tanque_Aquecimento = int(random.uniform(0, 100))

    Quant_Agua_Tanque_Mistura = int(random.uniform(0, 1000))

    Quant_AguaQuente_Tanque_Mistura = int(random.uniform(0, 500))

    Quant_AguaFria_Tanque_Mistura = int(random.uniform(0, 500))

    Tempo_Processo_Tanque_Mistura = int(random.uniform(0, 60))

    Quant_Agua_Saida_Tanque_Mistura = int(random.uniform(0, 60))

      # print(Quant_Agua_Saida_Reservatorio, Quant_Bomba_1_Reservatorio, Quant_Bomba_2_Reservatorio, Vazao_Valvula1, Vazao_Valvula2, Quant_Agua_Tanque_Aquecimento, Tempo_Processo_Tanque_Aquecimento, Quant_Agua_Saida_Tanque_Aquecimento, Temp_Agua_Tanque_Aquecimento, Quant_Agua_Tanque_Mistura, Quant_AguaQuente_Tanque_Mistura, Quant_AguaFria_Tanque_Mistura, Tempo_Processo_Tanque_Mistura, Quant_Agua_Saida_Tanque_Mistura)
    pacote = [10000 + Quant_Agua_Saida_Reservatorio, 20000 + Quant_Bomba_1_Reservatorio, 30000 + Quant_Bomba_2_Reservatorio, 40000 + Vazao_Valvula1, 50000 + Vazao_Valvula2, 60000 + Quant_Agua_Tanque_Aquecimento, 70000 + Tempo_Processo_Tanque_Aquecimento, 80000 +
    Quant_Agua_Saida_Tanque_Aquecimento, 90000 + Temp_Agua_Tanque_Aquecimento, 100000 + Quant_Agua_Tanque_Mistura, 110000 + Quant_AguaQuente_Tanque_Mistura, 120000 + Quant_AguaFria_Tanque_Mistura, 130000 + Tempo_Processo_Tanque_Mistura, 140000 + Quant_Agua_Saida_Tanque_Mistura]
    for i in pacote:
        if i < 100000:
            ser = serial.Serial('COM1')
            a = str(i)
            encoded = bytes("0"+a, 'utf-8')
            # print(encoded)
            ser.write(encoded)
            ser.close()
        else:
            ser = serial.Serial('COM1')
            a = str(i)
            encoded = bytes(a, 'utf-8')
            # print(encoded)
            ser.write(encoded)
            ser.close()

            print(Quant_Agua_Saida_Reservatorio, Quant_Bomba_1_Reservatorio, Quant_Bomba_2_Reservatorio, Vazao_Valvula1, Vazao_Valvula2, Quant_Agua_Tanque_Aquecimento, Tempo_Processo_Tanque_Aquecimento,
            Quant_Agua_Saida_Tanque_Aquecimento, Temp_Agua_Tanque_Aquecimento, Quant_Agua_Tanque_Mistura, Quant_AguaQuente_Tanque_Mistura, Quant_AguaFria_Tanque_Mistura, Tempo_Processo_Tanque_Mistura, Quant_Agua_Saida_Tanque_Mistura)
            time.sleep(1)

import serial


def Quant_Agua_Reservatorio():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if int(a) < 20000:
        b = int(a) - 10000
        return str(b)


def Quant_Bomba_1_Reservatorio():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 30000 > int(a) > 20000:
        c = int(a) - 20000
        return str(c)


def Quant_Bomba_2_Reservatorio():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 40000 > int(a) > 30000:
        d = int(a) - 30000
        return str(d)



def Vazao_Valvula1():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 50000 > int(a) > 40000:
        e = int(a) - 40000
        return str(e)

def Vazao_Valvula2():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 60000 > int(a) > 50000:
        f = int(a) - 50000
        return str(f)


def Quant_Agua_Tanque_Aquecimento():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 70000 > int(a) > 60000:
        g = int(a) - 60000
        return str(g)

def Tempo_Processo_Tanque_Aquecimento():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 80000 > int(a) > 70000:
        h = int(a) - 70000
        return str(h)


def Quant_Agua_Saida_Tanque_Aquecimento():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 90000 > int(a) > 80000:
        i = int(a) - 80000
        return str(i)


def Temp_Agua_Tanque_Aquecimento():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 100000 > int(a) > 90000:
        j = int(a) - 90000
        return str(j)


def Quant_Agua_Tanque_Mistura():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 110000 > int(a) > 100000:
        k = int(a) - 100000
        return str(k)


def Quant_AguaQuente_Tanque_Mistura():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 120000 > int(a) > 110000:
        l = int(a) - 110000
        return str(l)


def Quant_AguaFria_Tanque_Mistura():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 130000 > int(a) > 120000:
        m = int(a) - 120000
        return str(m)


def Tempo_Processo_Tanque_Mistura():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 140000 > int(a) > 130000:
        n = int(a) - 130000
        return str(n)


def Quant_Agua_Saida_Tanque_Mistura():
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if 150000 > int(a) > 140000:
        o = int(a) - 140000
        return str(o)

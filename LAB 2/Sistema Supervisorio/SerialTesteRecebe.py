import serial
contador = 0
lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while contador < 14:

    ser = serial.Serial('COM2') #open virtual serial port
    a = ser.read(4) #write a string
    lista[contador] = int(a)
    contador += 1

    ser.close() #close port
print(lista)
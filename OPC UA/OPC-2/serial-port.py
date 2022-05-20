import serial
from serial import Serial
ser = serial.Serial('/dev/ttyACM0',9600)


while True:
	data = ser.readline(1000)
	a = int(data)
	print(a)
from opcua import Client
import serial
import time


url = "opc.tcp://192.168.0.18:4840"
client = Client(url)

client.connect()


arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    porc = client.get_node("ns=2;i=2")
    por = porc.get_value()
    a = str (por)
    value = write_read(a)
    print(a)

    time.sleep(1)

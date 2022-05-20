import serial
while True:
    ser = serial.Serial('COM1') #open virtual serial port
    print(ser.portstr) #check which port was realy used
    msg = "10"
    encoded = bytes(str(msg), 'utf-8')
    ser.write(encoded)#write a string
    ser.close() #close port

    if i < 10:
        print(ser.portstr, "1")
        encoded = bytes(str("000" + str(i)), 'utf-8')
    if i == 10:
        print(ser.portstr, "2")
        encoded = bytes(str("00" + str(i)), 'utf-8')
    if i < 100:
        print(ser.portstr, "3")
        encoded = bytes(str("00" + str(i)), 'utf-8')
    if i == 100:
        print(ser.portstr, "4")
        encoded = bytes(str("0" + str(i)), 'utf-8')
    if i < 1000:
        print(ser.portstr, "5")
        encoded = bytes(str("0" + str(i)), 'utf-8')

    if i == 1000:
        print(ser.portstr, "6")
        encoded = bytes(str(i), 'utf-8')
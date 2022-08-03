import serial

while True:
    ser = serial.Serial('COM2')
    a = ser.read(6)
    ser.close()
    if int(a) < 20000:
        b = int(a) - 10000
        print(int(b))
    if int(a) < 30000 and int(a) > 20000:
        c = int(a) - 20000
        print(int(c))

    if int(a) < 40000 and int(a) > 30000:
        d = int(a) - 30000
        print(int(d))

    if int(a) < 50000 and int(a) > 40000:
        e = int(a) - 40000
        print(int(e))

    if int(a) < 60000 and int(a) > 50000:
        f = int(a) - 50000
        print(int(f))

    if int(a) < 70000 and int(a) > 60000:
        g = int(a) - 60000
        print(int(g))

    if int(a) < 80000 and int(a) > 70000:
        h = int(a) - 70000
        print(int(h))

    if int(a) < 90000 and int(a) > 80000:
        i = int(a) - 80000
        print(int(i))

    if int(a) < 100000 and int(a) > 90000:
        j = int(a) - 90000
        print(int(j))

    if int(a) < 110000 and int(a) > 100000:
        k = int(a) - 100000
        print(int(k))

    if int(a) < 120000 and int(a) > 110000:
        l = int(a) - 110000
        print(int(l))

    if int(a) < 130000 and int(a) > 120000:
        m = int(a) - 120000
        print(int(m))

    if int(a) < 140000 and int(a) > 130000:
        n = int(a) - 130000
        print(int(n))

    if int(a) < 150000 and int(a) > 140000:
        o = int(a) - 140000
        print(int(o))

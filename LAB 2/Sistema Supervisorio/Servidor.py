import serial
from pyModbusTCP.server import DataBank, ModbusServer
import time

class ServidorMODBUS():



    def __init__(self, host_ip, port):
        """
        Construtor
        """
        self._server = ModbusServer(host=host_ip, port=port, no_block=True)
        self._db = DataBank

    def run(self):
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start()
            print("Servidor MODBUS em execução")
            while True:
                contador = 0
                if contador < 14:
                    ser = serial.Serial('COM2')
                    a = ser.read(6)
                    ser.close()
                    if int(a) < 20000:
                        self._db.set_words(1, [int(a) - 10000])
                        print("PACOTE 1")
                    if int(a) < 30000 and int(a) > 20000:
                        self._db.set_words(5, [int(a) - 20000])
                        print("PACOTE 2")
                    if int(a) < 40000 and int(a) > 30000:
                        self._db.set_words(10, [int(a) - 30000])
                        print("PACOTE 3")
                    if int(a) < 50000 and int(a) > 40000:
                        self._db.set_words(20, [int(a) - 40000])
                        print("PACOTE 4")
                    if int(a) < 60000 and int(a) > 50000:
                        self._db.set_words(25, [int(a) - 50000])
                        print("PACOTE 5")
                    if int(a) < 70000 and int(a) > 60000:
                        self._db.set_words(30, [int(a) - 60000])
                        print("PACOTE 6")
                    if int(a) < 80000 and int(a) > 70000:
                        self._db.set_words(35, [int(a) - 70000])
                        print("PACOTE 7")
                    if int(a) < 90000 and int(a) > 80000:
                        self._db.set_words(40, [int(a) - 80000])
                        print("PACOTE 8")
                    if int(a) < 100000 and int(a) > 90000:
                        self._db.set_words(45, [int(a) - 90000])
                        print("PACOTE 9")
                    if int(a) < 110000 and int(a) > 100000:
                        self._db.set_words(50, [int(a) - 100000])
                        print("PACOTE 10")
                    if int(a) < 120000 and int(a) > 110000:
                        self._db.set_words(55, [int(a) - 110000])
                        print("PACOTE 11")
                    if int(a) < 130000 and int(a) > 120000:
                        self._db.set_words(60, [int(a) - 120000])
                        print("PACOTE 12")
                    if int(a) < 140000 and int(a) > 130000:
                        self._db.set_words(65, [int(a) - 130000])
                        print("PACOTE 13")
                    if int(a) < 150000 and int(a) > 140000:
                        self._db.set_words(70, [int(a) - 140000])
                        print("PACOTE 14")

                    contador += 1
                contador = 0
        except Exception as e:
            print("Erro: ", e.args)



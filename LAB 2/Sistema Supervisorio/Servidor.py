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

                    if 30000 > int(a) > 20000:
                        self._db.set_words(5, [int(a) - 20000])
                        print("PACOTE 2")

                    if 40000 > int(a) > 30000:
                        self._db.set_words(10, [int(a) - 30000])
                        print("PACOTE 3")

                    if 50000 > int(a) > 40000:
                        self._db.set_words(20, [int(a) - 40000])
                        print("PACOTE 4")

                    if 60000 > int(a) > 50000:
                        self._db.set_words(25, [int(a) - 50000])
                        print("PACOTE 5")

                    if 70000 > int(a) > 60000:
                        self._db.set_words(30, [int(a) - 60000])
                        print("PACOTE 6")

                    if 80000 > int(a) > 70000:
                        self._db.set_words(35, [int(a) - 70000])
                        print("PACOTE 7")

                    if 90000 > int(a) > 80000:
                        self._db.set_words(40, [int(a) - 80000])
                        print("PACOTE 8")

                    if 100000 > int(a) > 90000:
                        self._db.set_words(45, [int(a) - 90000])
                        print("PACOTE 9")

                    if 110000 > int(a) > 100000:
                        self._db.set_words(50, [int(a) - 100000])
                        print("PACOTE 10")

                    if 120000 > int(a) > 110000:
                        self._db.set_words(55, [int(a) - 110000])
                        print("PACOTE 11")

                    if 130000 > int(a) > 120000:
                        self._db.set_words(60, [int(a) - 120000])
                        print("PACOTE 12")

                    if 140000 > int(a) > 130000:
                        self._db.set_words(65, [int(a) - 130000])
                        print("PACOTE 13")

                    if 150000 > int(a) > 140000:
                        self._db.set_words(70, [int(a) - 140000])
                        print("PACOTE 14")

                    contador += 1
                contador = 0
        except Exception as e:
            print("Erro: ", e.args)

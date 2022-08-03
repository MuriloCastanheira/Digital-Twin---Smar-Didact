import mysql.connector
from mysql.connector import Error
import time


def dados_back():
    try:
        con = mysql.connector.connect(host='localhost', database='dados', user='root', passwd='')

        consulta_sql = "select * from datalogger"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        total = cursor.rowcount

        for linha in linhas:

            dados = [linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14]]
            return dados

    except Error as e:
        print("Error ao acessar tabela MySQL")
    finally:
        if con.is_connected():
            con.close()
            cursor.close()
            print("Conexão encerrada")
    time.sleep(2)

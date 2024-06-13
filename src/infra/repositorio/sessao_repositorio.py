import sqlite3
from typing import Tuple, List

import mysql.connector

from src.dominio.entidade import Sessao


class SessaoRepositorio:

    def __init__(self):
        self.__my_db_source = "mysql"

    def salva(self, sessao: Sessao):
        if self.__my_db_source == "sqlite":
            try:
                with sqlite3.connect('storage.db') as con:
                    cursor = con.cursor()
                    sql = "INSERT INTO sessao(codigo, nome, descricao, localizacao) VALUES(\'{}\', \'{}\', \'{}\', \'{}\')"
                    sql = sql.format(sessao.codigo, sessao.nome, sessao.descricao, sessao.localizacao)
                    cursor.execute(sql)
            except sqlite3.Error as e:
                print(e)

        else:
            connection = mysql.connector.connect(user='root', password='root'
                                                            , host='localhost'
                                                            , database='renato')

            mycursor = connection.cursor()

            sql = "INSERT INTO sessao(codigo, nome, descricao, localizacao) VALUES (%s, %s, %s, %s)"
            val = (sessao.codigo, sessao.nome, sessao.descricao, sessao.localizacao)
            mycursor.execute(sql, val)

            connection.commit()


    def get_sessoes(self) -> List[Tuple]:
        if self.__my_db_source == "sqlite":
            try:
                with sqlite3.connect('storage.db') as con:
                    cursor = con.cursor()
                    cursor.execute('select * from sessao')
                    rows = cursor.fetchall()
                    return rows
            except sqlite3.Error as e:
                print(e)

        else:
            connection = mysql.connector.connect(user='root'
                                                 , password='root'
                                                 , host='localhost'
                                                 , database='renato')

            my_cursor = connection.cursor()

            my_cursor.execute("SELECT * FROM sessao")

            my_result = my_cursor.fetchall()

            return my_result




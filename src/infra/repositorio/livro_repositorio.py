import sqlite3
from typing import List, Tuple

from src.dominio.entidade import Livro
import mysql.connector


class LivroRepositorio:
    def __init__(self):
        self.__my_db_source = "mysql"


    def salva(self, livro: Livro) -> None:
        if self.__my_db_source == "sqlite":
            try:
                with sqlite3.connect('storage.db') as con:
                    cursor = con.cursor()
                    sql = "INSERT INTO livro(codigo, titulo, autor, codigo_sessao) VALUES(\'{}\', \'{}\', \'{}\', \'{}\')"
                    sql = sql.format(livro.codigo, livro.titulo, livro.autor, livro.codigo_sessao)
                    cursor.execute(sql)
            except sqlite3.Error as e:
                print(e)

        else:
            connection = mysql.connector.connect(user='root'
                                                 , password='root'
                                                 , host='localhost'
                                                 , database='renato')

            mycursor = connection.cursor()

            sql = "INSERT INTO livro(codigo, titulo, autor, codigo_sessao) VALUES (%s, %s, %s, %s)"
            val = (livro.codigo, livro.titulo, livro.autor, livro.codigo_sessao)
            mycursor.execute(sql, val)

            connection.commit()


    def get_livros(self) -> List[Tuple]:
        if self.__my_db_source == "sqlite":
            try:
                with sqlite3.connect('storage.db') as con:
                    cursor = con.cursor()
                    cursor.execute('select * from livro')
                    rows = cursor.fetchall()
                    return rows
            except sqlite3.Error as e:
                print(e)
        else:
            connection = mysql.connector.connect(user='root'
                                                 , password='root'
                                                 , host='localhost'
                                                 , database='renato')

            mycursor = connection.cursor()

            mycursor.execute("SELECT * FROM livro")

            myresult = mycursor.fetchall()

            return myresult

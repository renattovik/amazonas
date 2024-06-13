import mysql.connector
import sqlite3
from sqlite3 import Error


def testando_mysql():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='renato')

    try:
        cursor = cnx.cursor()
        cursor.execute("""
        select * from livro
        """)
        result = cursor.fetchall()
        print(result)
    finally:
        cnx.close()


def sqlite_connection():
    try:
        con = sqlite3.connect('storage.db')
        return con
    except Error:
        print(Error)


def create_table_and_insert(con):
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS sessao")
    cursor.execute("DROP TABLE IF EXISTS livro")

    cursor.execute("CREATE TABLE sessao(codigo integer, nome varchar(100), descricao varchar(100), localizacao varchar(100));")
    cursor.execute("CREATE TABLE livro(codigo integer, titulo varchar(100), autor varchar(100), codigo_sessao integer);")

    cursor.execute("INSERT INTO sessao(codigo, nome, descricao, localizacao) VALUES('1', 'Ficcao cientifica', 'nda', 'C10L10P001')")
    cursor.execute("INSERT INTO livro(codigo, titulo, autor, codigo_sessao) VALUES('1', 'Era os Deuses Astronautas', 'Erik Von Danniken', '1')")

    cursor.execute("DELETE FROM sessao")
    cursor.execute("DELETE FROM livro")


def select_all_lines_from_table(conn, table):
    cur = conn.cursor()
    cur.execute('select * from {}'.format(table))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def testando_sqlite():
    try:
        with sqlite_connection() as conn:
            create_table_and_insert(conn)
            select_all_lines_from_table(conn, "livro")
            select_all_lines_from_table(conn, "sessao")

    except sqlite3.Error as e:
        print(e)


def main():
    # testando_mysql()
    testando_sqlite()


if __name__ == "__main__":
    main()

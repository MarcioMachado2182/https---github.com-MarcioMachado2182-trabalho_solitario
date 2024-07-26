# model/usuario_m.py
import mysql.connector
from mysql.connector import Error

class UsuarioModel:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='marcio_2182',
                password='2182',
                database='trabalho_db'
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def register_user(self, nome, endereco, email, senha):
        try:
            query = "INSERT INTO usuarios (nome, endereco, email, senha) VALUES (%s, %s, %s, %s)"
            values = (nome, endereco, email, senha)
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except Error as e:
            print(f"Erro ao registrar usuário: {e}")
            return False

    def close_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()



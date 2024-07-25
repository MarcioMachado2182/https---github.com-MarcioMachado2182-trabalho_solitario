import mysql.connector
from mysql.connector import Error

class BancoController:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Conecta ao banco de dados MariaDB e cria a tabela de usuários se necessário"""
        try:
            self.conn = mysql.connector.connect(
                host='3306',         # Substitua pelo seu host
                user='marcio_2182',              # Substitua pelo seu usuário
                password='123',  # Substitua pela sua senha
                database='trabalho_db'   # Substitua pelo seu banco de dados
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    endereco VARCHAR(255),
                    email VARCHAR(255) NOT NULL UNIQUE,
                    senha VARCHAR(255) NOT NULL
                )
            ''')
            self.conn.commit()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def register_user(self, nome, endereco, email, senha):
        """Registra um novo usuário no banco de dados"""
        try:
            self.cursor.execute('''
                INSERT INTO users (nome, endereco, email, senha)
                VALUES (%s, %s, %s, %s)
            ''', (nome, endereco, email, senha))
            self.conn.commit()
            return True
        except mysql.connector.IntegrityError:
            return False
        except Error as e:
            print(f"Erro ao registrar o usuário: {e}")
            return False

    def validate_user(self, email, senha):
        """Valida um usuário com base no e-mail e senha"""
        try:
            self.cursor.execute('''
                SELECT * FROM users WHERE email = %s AND senha = %s
            ''', (email, senha))
            result = self.cursor.fetchone()
            return result is not None
        except Error as e:
            print(f"Erro ao validar o usuário: {e}")
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

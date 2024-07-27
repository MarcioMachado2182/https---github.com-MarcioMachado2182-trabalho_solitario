# model/database.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='marcio_2182',
        password='2182',
        database='trabalho_db'
    )

def inserir_usuario(nome, endereco, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO usuarios (nome, endereco, email, senha) 
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, endereco, email, senha)

    try:
        cursor.execute(insert_query, valores)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False
    finally:
        cursor.close()
        conn.close()


import mysql.connector
from mysql.connector import Error


def bd_conectar():
    """
        Função utilizada para estabelecer a conexão com a base de dados,
        utilizando mysql.connector.
    """
    conexao = None
    try:
        conexao = mysql.connector.connect (
            host='localhost',
            user='root',
            password='senha',
            database='brasileirao'
        )
    
    except Error as e:
        print(f"Erro ao se conectar com o Banco de Dados: {e}")
         
    return conexao
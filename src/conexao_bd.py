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
        

    # CRUD

    # CREATE

    # nome_produto = "chocolate"
    # valor = 15

    # comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    # cursor.execute(comando)

    # conexao.commit() edita o banco de dados

    # READ

    # comando = 'select * from vendas'
    # cursor.execute(comando)

    # resultado = cursor.fetchall() # ler o banco de dados
    # print(resultado)

    # UPDATE

    # nome_produto = "todynho"
    # valor = 6
    # comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    # cursor.execute(comando)

    # conexao.commit() # edita o banco de dados

    # DELETE

    # nome_produto = "todynho"
    # comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    # cursor.execute(comando)
    # conexao.commit() # edita o banco de dados

    # cursor.close()
    # conexao.close()
    
    return conexao
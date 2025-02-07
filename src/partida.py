from mysql.connector import Error
from conexao_bd import bd_conectar


class Partida:
    """Classe utilizada para representar cada partida."""
    
    def __init__(self, data_inicio, id_mandante, id_visitante,
                resultado_mandante, resultado_visitante):
        self.data_inicio = data_inicio
        self.id_mandante = id_mandante
        self.id_visitante = id_visitante
        self.resultado_mandante = resultado_mandante
        self.resultado_visitante = resultado_visitante
    

def inserir_partida(partida):
    """Função utilizada para inserir uma nova partida."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir a partida no banco de dados:
    comando = f"""INSERT INTO partida (data_inicio, id_mandante, id_visitante,
            resultado_mandante, resultado_visitante)
            VALUES ("{partida.data_inicio}", {partida.id_mandante},
            {partida.id_visitante}, {partida.resultado_mandante},
            {partida.resultado_visitante},)"""
            
    try:
        cursor.execute(comando) # executa o respectivo comando
        conexao.commit() # edita o banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
    

def remover_partida(partida):
    """Função utilizada para remover uma partida."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para remover a partida no banco de dados:
    comando = f"""DELETE from partida WHERE id_partida = {partida.id_partida}"""
    
    try:
        cursor.execute(comando) # executa o respectivo comando
        conexao.commit() # edita o banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
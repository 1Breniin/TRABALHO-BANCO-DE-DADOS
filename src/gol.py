from mysql.connector import Error
from time import sleep
from jogador import jogador_pertence_clube
from exceptions import verifica_id, verifica_minuto


def insere_gols(id_partida, id_clube, cursor, conexao):
    """Função utilizada para inserir os gols em uma partida."""
    
    minuto = verifica_minuto()        
    while True:
        print(f"Agora, informe o ID do jogador que marcou o gol:")
        id_jogador = verifica_id()
        
        # Verifica se o jogador pertence ao clube que marcou o gol:
        if jogador_pertence_clube(id_jogador, id_clube, cursor):
            # Comando utilizado para inserir o gol na tabela gol:
            comando = """INSERT INTO gol (minuto, id_jogador, id_partida)
                    VALUES (%s, %s, %s)"""
                
            cursor.execute(comando, (minuto, id_jogador, id_partida,))
            conexao.commit() # edita o banco de dados
            break
        
        else:            
            print("ID do jogador inválido!\n")
    
    return minuto


def imprime_gols(id_partida, id_clube, cursor):
    """Função utilizada para imprimir os gols de uma partida."""
    
    # Comando utilizado para obter os dados do gols de uma partida:
    comando = """SELECT minuto, nome FROM gol JOIN jogador
            ON gol.id_jogador = jogador.id_jogador
            WHERE gol.id_partida = %s AND jogador.id_clube = %s
            ORDER BY minuto ASC"""
    
    try:
        cursor.execute(comando, (id_partida, id_clube)) # executa o respectivo comando
        resultado = cursor.fetchall() # leitura do banco de dados
        
        # Verifica se a query anterior obteve algum resultado:
        if resultado:
            # Imprime os gols marcados em uma partida:
            print("\n\t\tGols:")    
            for jogador in resultado:
                print(f"\t\t\t{jogador[0]}` {jogador[1]}")
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
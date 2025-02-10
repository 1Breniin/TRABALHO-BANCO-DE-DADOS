from mysql.connector import Error
from time import sleep
from jogador import jogador_pertence_clube, jogador_pertence_escalados
from exceptions import verifica_id


def insere_escalados(id_partida, id_clube, cursor, conexao):
    """Função utilizada para inserir os jogadores escalados em uma partida."""

    while True:
        id_jogador = verifica_id()
            
        if jogador_pertence_clube(id_jogador, id_clube, cursor) and not(jogador_pertence_escalados(id_jogador, id_partida, cursor)):
            comando = """INSERT INTO escalados (id_partida, id_jogador)
                    VALUES (%s, %s)"""
               
            cursor.execute(comando, (id_partida, id_jogador,))
            conexao.commit() # edita o banco de dados
            break
                
        else:
            print(f"O jogador com o ID {id_jogador} não pertence ao clube ou já foi escalado! Tente novamente...\n")
            sleep(1)
            
    
def imprime_escalados(id_partida, id_clube, cursor):
    """Função utilzada para imprimir os jogadores escalados de uma partida."""
    
    comando = """SELECT nome, numero_camisa, posicao FROM escalados
            JOIN jogador ON escalados.id_jogador = jogador.id_jogador
            WHERE escalados.id_partida = %s AND jogador.id_clube = %s"""
    
    try:
        cursor.execute(comando, (id_partida, id_clube)) # executa o respectivo comando
        resultado = cursor.fetchall() # leitura do banco de dados
        print("\t\tEscalação:")    
        for jogador in resultado:
            print(f"\t\t\t{jogador[1]} {jogador[0]} ({jogador[2]})")
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")

from mysql.connector import Error
from time import sleep
from jogador import jogador_pertence_clube
from exceptions import verifica_id


def insere_assistencia(id_clube, minuto, cursor, conexao):
    """Função utilizada para inserir os gols em uma partida."""
    
    while True:
        assistencia = input("Houve assistência (S/N): ").strip().capitalize()
        
        if assistencia == 'S':
            print("Agora, informe o ID do jogador que deu a assistência:")
            id_jogador = verifica_id()
                 
            if jogador_pertence_clube(id_jogador, id_clube, cursor):
                comando = """INSERT INTO assistencia (minuto, id_jogador)
                VALUES (%s, %s)"""
                
                cursor.execute(comando, (minuto, id_jogador,))
                conexao.commit() # edita o banco de dados
                break
                
            else:            
                print("ID do jogador inválido!\n")
                sleep(1)
            
        elif assistencia == 'N':
            break
            
        else:
            print("Por favor, digite S ou N!")
            sleep(1)
from mysql.connector import Error
from time import sleep
from jogador import jogador_pertence_clube
from exceptions import verifica_id, verifica_minuto


def insere_cartao(id_partida, id_clube, cursor, conexao):
    """Função utilizada para inserir os cartões em uma partida."""
    
    while True:
        try:
            num_cartoes = int(input("Tiveram quantos cartões?: "))

        except ValueError:
            print("Valor inválido!")
        
        else:
            if num_cartoes >= 0 and num_cartoes <= 22:
                break
            
            else:
                print("Número de cartões não permitido!")
    
    if num_cartoes > 0:
        print("Agora, informe o ID do jogador que levou o cartão, com quantos minutos foi e qual a cor do cartão (A: amarelo ou V: vermelho):")
        
    for _ in range(num_cartoes):
        id_jogador = verifica_id()
        minuto = verifica_minuto()
        
        while True:
            tipo = input("\tCor: ").strip().capitalize()
            
            if tipo != 'A' and tipo != 'V':
                print("Cor do cartão inválida! Digite 'A' ou 'V'...")
                sleep(1) 
            
            else:
                if jogador_pertence_clube(id_jogador, id_clube, cursor):
                    comando = """INSERT INTO cartao (tipo, minuto, id_jogador, id_partida)
                        VALUES (%s, %s, %s, %s)"""
                
                    cursor.execute(comando, (tipo, minuto, id_jogador, id_partida))
                    conexao.commit() # edita o banco de dados
                    break
                
                else:            
                    print("ID do jogador inválido!\n")


def imprime_cartoes_vermelhos(id_partida, id_clube, cursor):
    """Função utilzada para imprimir os cartões vermelhos de uma partida."""
    
    comando = """SELECT minuto, nome, tipo FROM cartao JOIN jogador
            ON cartao.id_jogador = jogador.id_jogador
            WHERE cartao.id_partida = %s AND jogador.id_clube = %s 
            AND cartao.tipo = 'V' 
            ORDER BY minuto ASC"""
    
    try:
        cursor.execute(comando, (id_partida, id_clube)) # executa o respectivo comando
        resultado = cursor.fetchall() # leitura do banco de dados
        
        if resultado:
            print("\n\t\tCartões Vermelhos:")    
            for jogador in resultado:
                print(f"\t\t\t{jogador[0]}` {jogador[1]}")
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
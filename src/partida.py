from mysql.connector import Error
from time import sleep
from conexao_bd import bd_conectar
from exceptions import verifica_id, verifica_resultado
from clube import existe_clube
from escalados import insere_escalados, imprime_escalados
from gol import insere_gols, imprime_gols
from assistencia import insere_assistencia
from cartao import insere_cartao, imprime_cartoes_vermelhos


class Partida:
    """Classe utilizada para representar cada partida."""
    
    def __init__(self, data_inicio, id_mandante, id_visitante,
                resultado_mandante, resultado_visitante):
        self.data_inicio = data_inicio
        self.id_mandante = id_mandante
        self.id_visitante = id_visitante
        self.resultado_mandante = resultado_mandante
        self.resultado_visitante = resultado_visitante
        
        
def partida_input():
    """
        Função utilizada para ler as informações digitadas pelo usuário a
        respeito de qual partida a query será executada.
    """
    
    data_inicio = input("Data de início (YYYY-MM-DD): ").strip()

    # Enquanto os dados de entrada não forem válidos: 
    while True:
        print("A seguir, informe o ID do clube mandante:")
        id_mandante = verifica_id()
        print("Já agora, informe o ID do clube visitante:")
        id_visitante = verifica_id()

        # Verifica se os clubes da partida não existem ou se eles são os
        # mesmos clubes:
        if not(existe_clube(id_mandante)) or not(existe_clube(id_visitante)) or id_mandante == id_visitante:
            print("Dados inválidos! Tente novamente...\n")
            sleep(1)
            continue
                
        else:
            print("Agora, informe o resultado do time mandante:")
            resultado_mandante = verifica_resultado()
            print("Por fim, informe o resultado do time visitante:")
            resultado_visitante = verifica_resultado()
            
            # Criação de um objeto partida com os dados digitados pelo usuário:
            partida = Partida(data_inicio, id_mandante, id_visitante,
                            resultado_mandante,resultado_visitante)
            return partida
        
        
def partida_disputada(id_mandante, id_visitante, cursor, conexao):
    """
        Função utilizada para verificar se um determinado clube já disputou uma
        determinada partida.
    """    

    # Comando utilizado para obter o número de partidas realizadas entre os
    # clubes, nas quais o mandante é id_mandante e o visitante é id_visitante:
    comando = """SELECT COUNT(*) FROM partida
            WHERE (id_mandante = %s AND id_visitante = %s)"""
    
    try:
        # Executa o respectivo comando: 
        cursor.execute(comando, (id_mandante, id_visitante,))
        partida_disputada = cursor.fetchone()[0] # leitura do banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
        
    if partida_disputada > 0:
        return True

    return False


def contar_num_partida(id_clube, cursor, conexao):
    """
        Função utilizada para verificar se um determinado clube já disputou
        todas as 38 partidas.
    """  
    
    # Comandos utilizados para contar o número de partidas do clube:
    comando_mandante = """SELECT COUNT(*) FROM partida 
                WHERE id_mandante = %s"""
    comando_visitante = """SELECT COUNT(*) FROM partida 
                WHERE id_visitante = %s"""
    
    try:
        # Executa o respectivo comando: 
        cursor.execute(comando_mandante, (id_clube,))
        # Leitura do banco de dados:
        num_partidas_mandante = cursor.fetchone()[0]
        # Executa o respectivo comando: 
        cursor.execute(comando_visitante, (id_clube,))
        # Leitura do banco de dados:
        num_partidas_visitante = cursor.fetchone()[0]
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
        
    return num_partidas_mandante + num_partidas_visitante

            
def inserir_dados_partida(id_partida, partida, cursor, conexao):
    """Função utilizada para inserir todos os dados de uma partida."""
    
    print("\nInforme os 11 jogadores escalados do time mandante:\n")
    for i in range(11):
        insere_escalados(id_partida, partida.id_mandante, cursor, conexao)
        
    print("\nInforme os 11 jogadores escalados do time visitante:\n")
    for i in range(11):
        insere_escalados(id_partida, partida.id_visitante, cursor, conexao)
            
    print("\nInforme os gols, assistências e cartões do time mandante:\n")
    for i in range(partida.resultado_mandante):
        print(f"GOL {i+1}")
        minuto = insere_gols(id_partida, partida.id_mandante, cursor, conexao)
        insere_assistencia(partida.id_mandante, minuto, cursor, conexao)
        insere_cartao(id_partida, partida.id_mandante, cursor, conexao)
        
    print("\nInforme os gols, assistências e cartões do time visitante:\n")
    for i in range(partida.resultado_visitante):
        print(f"GOL {i+1}")
        minuto = insere_gols(id_partida, partida.id_visitante, cursor, conexao)
        insere_assistencia(partida.id_visitante, minuto, cursor, conexao)
        insere_cartao(id_partida, partida.id_visitante, cursor, conexao)
        

def remover_dados_partida(id_partida, cursor, conexao):
    """Função utilizada para remover todos os dados de uma partida."""
    
    # Comandos utilizados para remover os dados de uma partida a respeito dos
    # jogadores escalados, dos gols marcados e das assistências:
    comando_escalados = """DELETE from escalados WHERE id_partida = %s"""
    comando_gol = """DELETE from gol WHERE id_partida = %s"""
    comando_assistencia = """DELETE FROM assistencia WHERE id_jogador IN
                (SELECT id_jogador FROM escalados WHERE id_partida = %s)"""
    
    try:
        # Executa o respectivo comando:
        cursor.execute(comando_escalados, (id_partida,))
        cursor.execute(comando_gol, (id_partida,))
        cursor.execute(comando_assistencia, (id_partida,))
        conexao.commit() # edita o banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")


def existe_partida(id_partida):
    """
        Função utilizada para verificar se um determinado id_partida existe na
        tabela partida.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter o número de partidas com id_partida:
    comando = """SELECT COUNT(*) FROM partida WHERE id_partida = %s"""
    
    existe = False
    try:
        cursor.execute(comando, (id_partida,)) # executa o respectivo comando
        numero_partidas = cursor.fetchone()[0] # leitura do banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

    if numero_partidas > 0:
        existe = True
    
    return existe


def inserir_partida(partida):
    """Função utilizada para inserir uma nova partida."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Primeiramente, verifica se a partida já não foi disputada:
    if not(partida_disputada(partida.id_mandante, partida.id_visitante, cursor, conexao)):
        # Em seguida, verifica se os clubes já não jogaram as 38 partidas:
        if contar_num_partida(partida.id_mandante, cursor, conexao) < 38 and contar_num_partida(partida.id_visitante, cursor, conexao) < 38:
        
            # Comando para inserir a partida no banco de dados:
            comando = """INSERT INTO partida (data_inicio, id_mandante, id_visitante,
                    resultado_mandante, resultado_visitante)
                    VALUES (%s, %s, %s, %s, %s)"""
                            
            try:
                # Executa o respectivo comando:
                cursor.execute(comando, (partida.data_inicio, partida.id_mandante,
                                        partida.id_visitante,
                                        partida.resultado_mandante,
                                        partida.resultado_visitante,))
                conexao.commit() # edita o banco de dados
                        
                # Obtém o id da partida:
                id_partida = cursor.lastrowid
                inserir_dados_partida(id_partida, partida, cursor, conexao)

            except Error as e:
                print(f"Erro ao realizar a query: {e}")
                
            else:
                print("\nA partida foi inserida com sucesso!\n")
                
            finally:
                cursor.close() # fechando o cursor
                conexao.close() # fechando a conexão

        else:
            print("\nUm dos clube já disputou todas as 38 partidas!\n")
        
    else:
        print("\nNão foi possível inserir essa partida pois, ela já ocorreu!\n")
    

def remover_partida(id_partida):
    """Função utilizada para remover uma partida."""
    
    if existe_partida(id_partida):
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
        
        # Comando para remover a partida no banco de dados:
        comando = """DELETE from partida WHERE id_partida = %s"""
        
        try:
            # Executa o respectivo comando:
            cursor.execute(comando, (id_partida,))
            conexao.commit() # edita o banco de dados
        
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
            
        else:
            print(f"\nA partida com ID {id_partida} foi removida com sucesso!\n")
            
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão

    else:
        print(f"\nA partida com o ID {id_partida} não existe!\n")
        

def atualizar_partida(id_partida):
    """Função utilizada para atualizar as informações de uma partida."""
    
    # Primeiramente, verifica se a partida existe:
    if existe_partida(id_partida):
        print(f"Informações atualizadas da partida com ID {id_partida}:\n")
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
            
        # Lê as novas informações para a partida:
        partida_atualizada = partida_input()
        
        # Comando utilizado para atualizar as informações da partida:
        comando = """UPDATE partida SET data_inicio = %s, id_mandante = %s,
                id_visitante = %s, resultado_mandante = %s, resultado_visitante = %s
                WHERE id_partida = %s"""

        try:
            # Executa o respectivo comando:
            cursor.execute(comando, (partida_atualizada.data_inicio, 
                                     partida_atualizada.id_mandante, 
                                     partida_atualizada.id_visitante, 
                                     partida_atualizada.resultado_mandante, 
                                     partida_atualizada.resultado_visitante, 
                                     id_partida,))
            
            conexao.commit() # edita o banco de dados
            
            # Comando utilizada para obter as informações de uma id_partida:
            comando = """SELECT data_inicio, id_mandante, id_visitante, resultado_mandante,
                    resultado_visitante FROM partida WHERE id_partida = %s"""
                    
            cursor.execute(comando, (id_partida,)) # executa o respectivo comando
            resultado = cursor.fetchone() # leitura do banco de dados
         
            # Enquanto as novas informações forem fornecidas ou se não houver
            # novos dados:
            while True:   
                mudancas = input("Ocorreram mudanças nos escalados, gols, cartões ou assistências? (S/N): ").strip().capitalize()
                
                # Verifica se houve mudanças no dados da partida:
                if mudancas == 'S':
                    remover_dados_partida(id_partida, cursor, conexao)
                    
                    partida = Partida(resultado[0], resultado[1], resultado[2], 
                              resultado[3], resultado[4])  
                    inserir_dados_partida(id_partida, partida, cursor, conexao)
                    break
                
                elif mudancas == 'N':
                    break
                
                else:
                    print("Opção inválida! Digite 'S' ou 'N'...\n")
                    sleep(1)
                
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
                
        else:
            print(f"\nA partida com ID {id_partida} foi atualizada com sucesso!\n")
                
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    
    else:
        print(f"\nA partrida com o ID {id_partida} não existe!\n")


def buscar_partidas(nome_clube):
    """Função utilizada para obter as informações das partidas de um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter o id_clube de acordo com o nome do clube:
    comando = """SELECT id_clube FROM clube  WHERE nome = %s"""
    
    try:
        cursor.execute(comando, (nome_clube,)) # executa o respectivo comando
        resultado = cursor.fetchone() # leitura do banco de dados
        
        # Se a query anterior obteve algum resultado
        if resultado:
            id_clube = resultado[0] # obtém o id_clube do resultado da query
            
            # Comando para obter todas as partidas de um determinado clube:
            comando = """SELECT id_partida, data_inicio, mandante.nome,
                    visitante.nome, resultado_mandante, resultado_visitante
                    FROM partida
                    JOIN clube mandante ON id_mandante = mandante.id_clube
                    JOIN clube visitante ON id_visitante = visitante.id_clube
                    WHERE id_mandante = %s OR id_visitante = %s
                    ORDER BY data_inicio ASC"""
            
            # Executa o respectivo comando:
            cursor.execute(comando, (id_clube, id_clube,))
            partidas = cursor.fetchall() # leitura do banco de dados
            
            # Verifica se o clube já disputou partidas:
            if partidas:
                # Imprime cada partida do clube:
                print(f"\nPartidas do clube {nome_clube}:\n")
                for partida in partidas:
                    print(f"\tID: {partida[0]}\n\tData de início: {partida[1]}\n\t{partida[2]} {partida[4]} X {partida[5]} {partida[3]}\n")
                    
                    imprime_escalados(partida[0], id_clube, cursor)
                    imprime_gols(partida[0], id_clube, cursor)
                    imprime_cartoes_vermelhos(partida[0], id_clube, cursor)
                
            else:
                print(f"\nO clube {nome_clube} não disputou nenhuma partida!\n")
                
        else:
            print(f"\nO clube {nome_clube} não foi encontrado!\n")   

    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
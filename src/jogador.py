from mysql.connector import Error
from time import sleep
from conexao_bd import bd_conectar
from exceptions import verifica_numero_camisa, verifica_altura, verifica_id
from clube import existe_clube


class Jogador:
    """Classe utilizada para representar cada jogador."""
    
    def __init__(self, nome, numero_camisa, data_nascimento, posicao, pe_bom,
                altura, id_clube, nacionalidade="Brasileiro"):
        self.nome = nome
        self.numero_camisa = numero_camisa
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.posicao = posicao
        self.pe_bom = pe_bom
        self.altura = altura
        self.id_clube = id_clube
        

def jogador_input():
    """
        Função utilizada para ler as informações digitadas pelo usuário a
        respeito de qual jogador a query será executada.
    """
    
    nome = input("Nome: ").strip().capitalize()
    numero_camisa = verifica_numero_camisa()
    
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ").strip()
    posicao = input("Posição: ").strip().capitalize()
    
    # Enquanto a variável pe_bom não for válida:
    while True:
        pe_bom = input("Pé bom (D ou E): ").strip().upper()
        if pe_bom in ['D', 'E']:
            break
        
        else:
            print("Digite um valor válido!\n")
    
    altura = verifica_altura()
    
    print("A seguir, informe o ID do clube do jogador:")
    # Enquanto o ID do clube do jogador não for válido:
    while True:
        id_clube = verifica_id()
        
        # Se o clube existir, o laço se encerra:
        if existe_clube(id_clube):
            break
        
        else:
            print(f"O clube com o ID {id_clube} não existe! Tente novamente...\n")
            sleep(1)
    
    nacionalidade = ''
    nacionalidade = input("Nacionalidade: ").strip().capitalize()
        
    # Criação de um objeto jogador com os dados digitados pelo usuário:
    jogador = Jogador(nome, numero_camisa, data_nascimento, posicao, pe_bom,
                      altura, id_clube, nacionalidade=nacionalidade)
    
    return jogador


def existe_jogador(id_jogador):
    """
        Função utilizada para verificar se um determinado id_jogador existe na
        tabela jogador.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para verificar se o jogador existe no banco de dados:
    comando = """SELECT COUNT(*) FROM jogador WHERE id_jogador = %s"""
    
    existe = False
    try:
        cursor.execute(comando, (id_jogador,)) # executa o respectivo comando
        numero_jogadores = cursor.fetchone()[0] # leitura do banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

    if numero_jogadores > 0:
        existe = True
    
    return existe


def jogador_pertence_clube(id_jogador, id_clube, cursor):
    """
        Função utilizada para verificar se um determinado id_jogador pertence
        a um id_clube.
    """
    
    # Comando utilizado para a obter a quantidade de jogadores com id_jogador
    # do id_clube na tabela jogador:
    comando = """SELECT COUNT(*) FROM jogador WHERE id_jogador = %s AND
            id_clube = %s"""
            
    cursor.execute(comando, (id_jogador, id_clube,))
    resultado = cursor.fetchone()[0]
    
    if resultado > 0:
        return True

    return False


def jogador_pertence_escalados(id_jogador, id_partida, cursor):
    """
        Função utilizada para verificar se um determinado id_jogador pertence
        aos escalados de uma determinada id_partida.
    """
    
    # Comando utilizado para a obter a quantidade de jogadores com id_jogador
    # na id_partida na tabela escalados:
    comando = """SELECT COUNT(*) FROM escalados WHERE id_jogador = %s AND
            id_partida = %s"""
            
    cursor.execute(comando, (id_jogador, id_partida,))
    resultado = cursor.fetchone()[0]
    
    if resultado > 0:
        return True

    return False
    
    
def inserir_jogador(jogador):
    """Função utilizada para inserir um novo jogador."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir o jogador no banco de dados:
    comando = """INSERT INTO jogador (nome, numero_camisa, nacionalidade,
            data_nascimento, posicao, pe_bom, altura, id_clube)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    try:
        # Executa o respectivo comando:
        cursor.execute(comando, (jogador.nome, jogador.numero_camisa,
                                 jogador.nacionalidade,
                                 jogador.data_nascimento, jogador.posicao,
                                 jogador.pe_bom, jogador.altura,
                                 jogador.id_clube,))
        conexao.commit() # edita o banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
    

def remover_jogador(id_jogador):
    """Função utilizada para remover um jogador."""
    
    # Primeiramente, verifica se o jogador existe:
    if existe_jogador(id_jogador):
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
        
        # Comando para remover o jogador do banco de dados:
        comando = """DELETE from jogador WHERE id_jogador = %s"""
        
        try:
            cursor.execute(comando, (id_jogador,)) # executa o respectivo comando
            conexao.commit() # edita o banco de dados
        
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
            
        else:
            print(f"\nO jogador com ID {id_jogador} foi removido com sucesso!\n")
            
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO jogador com o ID {id_jogador} não existe!\n")


def buscar_jogadores(nome_clube):
    """Função utilizada para obter os jogadores de um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter o id_clube de acordo com o nome do clube:
    comando = """SELECT id_clube FROM clube  WHERE nome = %s"""
        
    try:
        cursor.execute(comando, (nome_clube,)) # executa o respectivo comando
        resultado = cursor.fetchone() # leitura do banco de dados
        
        # Verifica se a query anterior possui algum resultado:    
        if resultado:
            id_clube = resultado[0] # obtém o id_clube do resultado da query
            
            # Comando para obter todos os jogadores de um determinado clube:
            comando = """SELECT id_jogador, nome, numero_camisa,
                    nacionalidade, data_nascimento, posicao, pe_bom, altura
                    FROM jogador WHERE id_clube = %s"""
                    
            cursor.execute(comando, (id_clube,)) # executa o respectivo comando
            jogadores = cursor.fetchall() # leitura do banco de dados
            
            # Verifica se o clube possui jogadores:
            if jogadores:
                # Imprime cada jogador do clube:
                print(f"\nJogadores do clube {nome_clube}:\n")
                for jogador in jogadores:
                    print(f"\tID: {jogador[0]}\n\tNome: {jogador[1]}\n\tNúmero da Camisa: {jogador[2]}\n\tNacionalidade: {jogador[3]}\n\tData de Nascimento: {jogador[4]}\n\tPosição: {jogador[5]}\n\tPé bom: {jogador[6]}\n\tAltura: {jogador[7]}\n")
            
            else:
                print(f"\nO clube {nome_clube} não possui nenhum jogador!\n")
            
        else:
            print(f"\nO clube {nome_clube} não foi encontrado!\n")      
            
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def atualizar_jogador(id_jogador):
    """Função utilizada para atualizar as informações de um jogador."""
    
    # Primeiramente, verifica se o jogador existe:
    if existe_jogador(id_jogador):
        print(f"Preencha as informações atualizadas do jogador com ID {id_jogador}:\n")
        
        conexao = bd_conectar()
        cursor = conexao.cursor()
            
        # Lê as novas informações para o jogador:
        jogador_atualizado = jogador_input()
        
        # Comando utilizado para atualizar as informações do jogador:
        comando = """UPDATE jogador SET nome = %s, numero_camisa = %s,
                data_nascimento = %s, posicao = %s, pe_bom = %s, altura = %s,
                id_clube = %s, nacionalidade = %s
                WHERE id_jogador = %s"""
            
        try:
            # Executa o respectivo comando:
            cursor.execute(comando, (jogador_atualizado.nome,
                                     jogador_atualizado.numero_camisa,
                                     jogador_atualizado.data_nascimento,
                                     jogador_atualizado.posicao,
                                     jogador_atualizado.pe_bom,
                                     jogador_atualizado.altura,
                                     jogador_atualizado.id_clube,
                                     jogador_atualizado.nacionalidade,
                                     id_jogador,))
            conexao.commit() # edita o banco de dados
            
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
                
        else:
            print(f"\nO jogador com ID {id_jogador} foi atualizado com sucesso!\n")
                
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO jogador com o ID {id_jogador} não existe!\n")
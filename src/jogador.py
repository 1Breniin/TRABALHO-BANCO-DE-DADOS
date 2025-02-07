from mysql.connector import Error
from conexao_bd import bd_conectar
from exceptions import verifica_numero_camisa, verifica_altura, verifica_id


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
    
    nome = input("Nome: ")
    numero_camisa = verifica_numero_camisa()
    
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    posicao = input("Posição: ")
    
    while True:
        pe_bom = input("Pé bom (D ou E): ").upper()
        if pe_bom in ['D', 'E']:
            break
        
        else:
            print("Digite um valor válido!")
    
    altura = verifica_altura()
    
    print("A seguir, informe o ID do clube do jogador:")
    id_clube = verifica_id()
    
    nacionalidade = ''
    nacionalidade = input("Nacionalidade: ")
        
    # Criação de um objeto jogador com os dados digitados pelo usuário:
    jogador = Jogador(nome, numero_camisa, data_nascimento, posicao, pe_bom, altura, id_clube, nacionalidade=nacionalidade)
    
    return jogador


def existe_jogador(id_jogador):
    """
        Função utilizada para verificar se um determinado id_jogador existe na
        tabela jogador.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para selecionar todos os jogadores do banco de dados:
    comando = f"""SELECT COUNT(*) FROM jogador WHERE id_jogador = {id_jogador}"""
    
    existe = False
    try:
        cursor.execute(comando) # executa o respectivo comando
        numero_jogadores = cursor.fetchone()[0] # leitura do banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

    if numero_jogadores > 0:
        existe = True
    
    return existe


def inserir_jogador(jogador):
    """Função utilizada para inserir um novo jogador."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir o jogador no banco de dados:
    comando = f"""INSERT INTO jogador (nome, numero_camisa, nacionalidade,
            data_nascimento, posicao, pe_bom, altura, id_clube)
            VALUES ('{jogador.nome}', {jogador.numero_camisa},
            '{jogador.nacionalidade}', '{jogador.data_nascimento}',
            '{jogador.posicao}', '{jogador.pe_bom}', {jogador.altura},
            {jogador.id_clube})"""
    
    try:
        cursor.execute(comando) # executa o respectivo comando
        conexao.commit() # edita o banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
    

def remover_jogador(id_jogador):
    """Função utilizada para remover um jogador."""
    
    if existe_jogador(id_jogador):
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
        
        # Comando para remover o jogador do banco de dados:
        comando = f"""DELETE from jogador WHERE id_jogador = {id_jogador}"""
        
        try:
            cursor.execute(comando) # executa o respectivo comando
            conexao.commit() # edita o banco de dados
        
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
            
        else:
            print(f"\nO jogador com ID {id_jogador} foi removido com sucesso!")
            
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO jogador com o ID {id_jogador} não existe!")


def buscar_jogadores(nome_clube):
    """Função utilizada para obter os jogadores de um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter o id_clube de acordo com o nome do clube:
    comando = f"""SELECT id_clube FROM clube  WHERE nome = '{nome_clube}'"""
        
    try:
        cursor.execute(comando) # executa o respectivo comando
        resultado = cursor.fetchone() # leitura do banco de dados
                
        if resultado:
            id_clube = resultado[0]
            
            # Comando para obter todos os jogadores de um determinado clube:
            comando = f"""SELECT id_jogador, nome, numero_camisa, nacionalidade, data_nascimento, posicao, pe_bom, altura FROM jogador WHERE id_clube = {id_clube}"""
                    
            cursor.execute(comando) # executa o respectivo comando
            jogadores = cursor.fetchall() # leitura do banco de dados
            
            if jogadores:
                print(f"\nJogadores do clube {nome_clube}:\n")
                for jogador in jogadores:
                    print(f"\tID: {jogador[0]}\n\tNome: {jogador[1]}\n\tNúmero da Camisa: {jogador[2]}\n\tNacionalidade: {jogador[3]}\n\tData de Nascimento: {jogador[4]}\n\tPosição: {jogador[5]}\n\tPé bom: {jogador[6]}\n\tAltura: {jogador[7]}\n")
            
            else:
                print(f"O clube {nome_clube} não possui nenhum jogador!\n")
            
        else:
            print(f"O clube {nome_clube} não foi encontrado!\n")      
            
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def atualizar_jogador(id_jogador):
    """Função utilizada para atualizar as informações de um jogador."""
    
    if existe_jogador(id_jogador):
        print(f"Preencha as informações atualizadas do jogador com ID {id_jogador}:\n")
        
        conexao = bd_conectar()
        cursor = conexao.cursor()
            
        jogador_atualizado = jogador_input()
        
        comando = f"""UPDATE jogador SET nome = '{jogador_atualizado.nome}', 
                numero_camisa = {jogador_atualizado.numero_camisa}, data_nascimento = '{jogador_atualizado.data_nascimento}', posicao = '{jogador_atualizado.posicao}', pe_bom = '{jogador_atualizado.pe_bom}', altura = {jogador_atualizado.altura}, id_clube = {jogador_atualizado.id_clube}, nacionalidade = '{jogador_atualizado.nacionalidade}' WHERE id_jogador = {id_jogador}"""
            
        try:
            cursor.execute(comando) # executa o respectivo comando
            conexao.commit() # edita o banco de dados
            
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
                
        else:
            print(f"\nO jogador com ID {id_jogador} foi atualizado com sucesso!")
                
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO jogador com o ID {id_jogador} não existe!")
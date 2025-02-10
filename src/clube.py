from mysql.connector import Error
from conexao_bd import bd_conectar


class Clube:
    """Classe utilizada para representar cada clube."""
    
    def __init__(self, nome, cidade, estado, estadio, maior_rival, tecnico):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.estadio = estadio
        self.maior_rival = maior_rival
        self.tecnico = tecnico
        
        
def clube_input():
    """
        Função utilizada para ler as informações digitadas pelo usuário a
        respeito de qual clube a query será executada.
    """
    
    nome = input("Nome: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()
    estadio = input("Estádio: ").strip()
    maior_rival = input("Maior rival: ").strip()
    tecnico = input("Técnico: ").strip()
    
    # Criação de um objeto clube com os dados digitados pelo usuário:
    clube = Clube(nome, cidade, estado, estadio, maior_rival, tecnico)
    
    return clube


def existe_clube(id_clube):
    """
        Função utilizada para verificar se um determinado id_clube existe na
        tabela clube.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para verificar se o clube existe no banco de dados:
    comando = """SELECT COUNT(*) FROM clube WHERE id_clube = %s"""
    
    existe = False
    try:
        cursor.execute(comando, (id_clube,)) # executa o respectivo comando
        numero_clubes = cursor.fetchone()[0] # leitura do banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

    if numero_clubes > 0:
        existe = True
    
    return existe


def inserir_clube(clube):
    """Função utilizada para inserir um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir o clube no banco de dados:
    comando = """INSERT INTO clube (nome, cidade, estado, estadio,
            maior_rival, tecnico) VALUES (%s, %s, %s, %s, %s, %s)"""
    
    try:
        # Executa o respectivo comando:
        cursor.execute(comando, (clube.nome, clube.cidade, clube.estado,
                                 clube.estadio, clube.maior_rival, 
                                 clube.tecnico,))
        conexao.commit() # edita o banco de dados
        
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    else:
        print(f"\nO clube {clube.nome} foi inserido com sucesso!")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def remover_clube(id_clube):
    """Função utilizada para remover um clube."""
    
    if existe_clube(id_clube):
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
        
        # Comando para remover o clube do banco de dados:
        comando = """DELETE FROM clube WHERE id_clube = %s"""
        
        try:
            cursor.execute(comando, (id_clube,)) # executa o respectivo comando
            conexao.commit() # edita o banco de dados
        
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
            
        else:
            print(f"\nO clube com ID {id_clube} foi removido com sucesso!")
            
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO clube com o ID {id_clube} não existe!")


def buscar_clube(nome):
    """Função utilizada para obter as informações de um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para selecionar o clube do banco de dados pelo nome:
    comando = """SELECT id_clube, cidade, estado, estadio, maior_rival, tecnico 
            FROM clube WHERE nome = %s"""
    
    try:
        cursor.execute(comando, (nome,)) # executa o respectivo comando
        informacoes = cursor.fetchone() # leitura do banco de dados
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
        
    if informacoes:
        print(f"\nInformações do clube {nome}:\n")
        print(f"\tID: {informacoes[0]}\n\tCidade: {informacoes[1]}\n\tEstado: {informacoes[2]}\n\tEstádio: {informacoes[3]}\n\tMaior rival: {informacoes[4]}\n\tTécnico: {informacoes[5]}\n")
    
    else:
        print(f"O clube {nome} não foi encontrado!\n")


def atualizar_clube(id_clube):
    """Função utilizada para atualizar as informações de um clube."""
    
    if existe_clube(id_clube):
        print(f"Informações atualizadas do clube com ID {id_clube}:\n")
    
        conexao = bd_conectar()
        cursor = conexao.cursor()
            
        clube_atualizado = clube_input()
            
        comando = """UPDATE clube SET nome = %s, cidade = %s, estado = %s,
                estadio = %s, maior_rival = %s, tecnico = %s
                WHERE id_clube = %s"""
            
        try:
            # Executa o respectivo comando:
            cursor.execute(comando, (clube_atualizado.nome,
                                     clube_atualizado.cidade,
                                     clube_atualizado.estado,
                                     clube_atualizado.estadio,
                                     clube_atualizado.maior_rival,
                                     clube_atualizado.tecnico, id_clube,))
            conexao.commit() # edita o banco de dados
            
        except Error as e:
            print(f"Erro ao realizar a query: {e}")
                
        else:
            print(f"\nO clube com ID {id_clube} foi atualizado com sucesso!")
                
        finally:
            cursor.close() # fechando o cursor
            conexao.close() # fechando a conexão
    
    else:
        print(f"\nO clube com o ID {id_clube} não existe!")
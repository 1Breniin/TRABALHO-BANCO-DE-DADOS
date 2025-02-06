from conexao_bd import bd_conectar

class Clube:
    """Classe utilizada para representar cada clube."""
    
    def __init__(self, nome, cidade, estado, estadio, maior_rival, tecnico, id_classificacao):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.estadio = estadio
        self.maior_rival = maior_rival
        self.tecnico = tecnico
        self.id_classificacao = id_classificacao
    

def inserir_clube(clube):
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir o clube no banco de dados:
    comando = f"""INSERT INTO clube (nome, cidade, estado, estadio, maior_rival,
            tecnico, id_classificacao) 
            VALUES ("{clube.nome}", {clube.cidade}, {clube.estado}, {clube.estadio},
            {clube.maior_rival}, {clube.tecnico}, {clube.id_classificacao})"""
    cursor.execute(comando) # executa o respectivo comando
    
    conexao.commit() # edita o banco de dados
    
    cursor.close() # fechando o cursor
    conexao.close() # fechando a conexão


def remover_clube(clube):
    """Função utilizada para remover um clube."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para remover o jogador no banco de dados:
    comando = f"""DELETE from jogador WHERE id_clube = {clube.id_clube}"""
    
    cursor.execute(comando) # executa o respectivo comando
    
    conexao.commit() # edita o banco de dados
    
    cursor.close() # fechando o cursor
    conexao.close() # fechando a conexão

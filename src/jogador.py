from conexao_bd import bd_conectar

class Jogador:
    """Classe utilizada para representar cada jogador."""
    
    def __init__(self, nome, numero_camisa, data_nascimento, posicao, pe_bom, altura, id_clube, nacionalidade="Brasileiro"):
        self.nome = nome
        self.numero_camisa = numero_camisa
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.posicao = posicao
        self.pe_bom = pe_bom
        self.altura = altura
        self.id_clube = id_clube
        

def inserir_jogador(jogador):
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para inserir o jogador no banco de dados:
    comando = f"""INSERT INTO jogador (nome, numero_camisa, nacionalidade, data_nascimento, 
            posicao, pe_bom, altura, id_clube) 
            VALUES ("{jogador.nome}", {jogador.numero_camisa}, {jogador.nacionalidade},
            {jogador.data_nascimento}, {jogador.posicao}, {jogador.pe_bom},
            {jogador.altura}, {jogador.id_clube})"""
    cursor.execute(comando) # executa o respectivo comando
    
    conexao.commit() # edita o banco de dados
    
    cursor.close() # fechando o cursor
    conexao.close() # fechando a conexão
    

def remover_jogador(jogador):
    """Função utilizada para remover um jogador."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para remover o jogador no banco de dados:
    comando = f"""DELETE from jogador WHERE id_jogador = {jogador.id_jogador}"""
    
    cursor.execute(comando) # executa o respectivo comando
    
    conexao.commit() # edita o banco de dados
    
    cursor.close() # fechando o cursor
    conexao.close() # fechando a conexão

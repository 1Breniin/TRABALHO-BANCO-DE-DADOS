from mysql.connector import Error
from conexao_bd import bd_conectar


def maiores_artilheiros():
    """Função utilizada para obter os jogadores que marcaram mais gols."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter os artilheiros do campeonato:
    comando = """SELECT jogador.nome, clube.nome, COUNT(id_gol) as numero_gols
            FROM jogador
            JOIN gol ON jogador.id_jogador = gol.id_jogador
            JOIN clube ON jogador.id_clube = clube.id_clube
            GROUP BY jogador.id_jogador
            ORDER BY numero_gols DESC"""
            
    try:
        cursor.execute(comando)
        jogadores = cursor.fetchall()
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
    
    else:
        # Se a query anterior retornou algum resultado:
        if jogadores:
            # Imprime os artilheiros do campeonato:
            print("-" * 90)
            print(f"{'Nome':^30}{'Clube':^30}{'Gols':^12}")
            print("-" * 90)
            for jogador in jogadores:
                print(f"{jogador[0]:^30}{jogador[1]:^30}{jogador[2]:^12}")
            print("-" * 90)
            
        else:
            print("\nNenhum jogador marcou gols ainda!\n")    
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def mais_assistencias():
    """Função utilizada para obter os jogadores que mais deram assistências."""
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter os jogadores com mais assistências no campeonato:
    comando = """SELECT jogador.nome, clube.nome, COUNT(id_assistencia)
            as numero_assistencias FROM jogador
            JOIN assistencia ON jogador.id_jogador = assistencia.id_jogador
            JOIN clube ON jogador.id_clube = clube.id_clube
            GROUP BY jogador.id_jogador
            ORDER BY numero_assistencias DESC"""

    try:
        cursor.execute(comando)
        jogadores = cursor.fetchall()
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
    
    else:
        # Se a query anterior retornou algum resultado:
        if jogadores:
            # Imprime os jogadores com mais assistências:
            print("-" * 90)
            print(f"{'Nome':^30}{'Clube':^30}{'Assistências':^12}")
            print("-" * 90)
            for jogador in jogadores:
                print(f"{jogador[0]:^30}{jogador[1]:^30}{jogador[2]:^12}")
            print("-" * 90)
            
        else:
            print("\nNenhum jogador deu nenhuma assistência ainda!\n")    
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
    

def mais_gols_acrescimos():
    """
        Função utilizada para obter os clubes que marcaram mais gols nos
        acréscimos.
    """ 

    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter os clubes com mais gols marcados nos acréscimos:
    comando = """SELECT clube.nome, COUNT(gol.id_gol) as total
            FROM clube
            JOIN jogador ON clube.id_clube = jogador.id_clube
            JOIN gol ON jogador.id_jogador = gol.id_jogador
            JOIN partida ON gol.id_partida = partida.id_partida
            WHERE gol.minuto > 90
            GROUP BY clube.id_clube
            ORDER BY total DESC"""
    
    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
    
    else:
        # Se a query anterior retornou algum resultado:
        if resultado:
            # Imprime os clubes com mais gols marcados nos acréscimos:
            print("-" * 70)
            print(f"{'Clube':^30}{'Total de Gols no Acréscimos':^30}")
            print("-" * 70)
            for clube in resultado:
                print(f"{clube[0]:^30}{clube[1]:^30}")
            print("-" * 70)
            
        else:
            print("\nNenhum clube possui jogador estrangeiro ainda!\n")    
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def maior_numero_cartoes():
    """
        Função utilizada para obter os jogadores que possuem o maior número
        de cartões amarelos e/ou vermelhos.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter os jogadores mais penalizados:
    comando = """SELECT j.nome AS jogador, c.nome AS clube,
            COUNT(CASE WHEN ct.tipo = 'A' THEN 1 END) AS cartoes_amarelos,
            COUNT(CASE WHEN ct.tipo = 'V' THEN 1 END) AS cartoes_vermelhos,
            COUNT(ct.id_cartao) AS total_cartoes
            FROM jogador j
            JOIN cartao ct ON j.id_jogador = ct.id_jogador
            JOIN clube c ON j.id_clube = c.id_clube
            GROUP BY j.id_jogador, c.nome
            ORDER BY total_cartoes DESC, cartoes_vermelhos DESC, cartoes_amarelos DESC"""
            
    try:
        cursor.execute(comando)
        jogadores = cursor.fetchall()
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
    
    else:
        # Se a query anterior retornou algum resultado:
        if jogadores:
            # Imprime os jogadores com mais cartões:
            print("-" * 120)
            print(f"{'Nome':^30}{'Clube':^30}{'Vermelhos':^20}{'Amarelos':^20}{'Total':^20}")
            print("-" * 120)
            for jogador in jogadores:
                print(f"{jogador[0]:^30}{jogador[1]:^30}{jogador[2]:^20}{jogador[3]:^20}{jogador[4]:^20}")
            print("-" * 120)
            
        else:
            print("\nNenhum jogador possui cartão ainda!\n")    
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão


def mais_estrangeiros():
    """
        Função utilizada para obter os clubes que possuem o maior número de
        jogadores estrangeiros.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando para obter os clubes com mais estrangeiros:
    comando = """SELECT clube.nome, COUNT(jogador.id_jogador) AS total 
            FROM clube 
            JOIN jogador ON clube.id_clube = jogador.id_clube
            WHERE jogador.nacionalidade != 'Brasileiro'
            GROUP BY clube.id_clube
            ORDER BY total DESC"""
    
    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()
    
    except Error as e:
        print(f"Erro ao realizar a query: {e}")
    
    else:
        # Se a query anterior retornou algum resultado:
        if resultado:
            # Imprime os clubes com mais jogadores estrangeiros:
            print("-" * 70)
            print(f"{'Clube':^30}{'Total de Estrangeiros':^30}")
            print("-" * 70)
            for clube in resultado:
                print(f"{clube[0]:^30}{clube[1]:^30}")
            print("-" * 70)
            
        else:
            print("\nNenhum clube possui jogador estrangeiro ainda!\n")    
                
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão
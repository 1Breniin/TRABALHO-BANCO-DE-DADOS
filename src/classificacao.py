from mysql.connector import Error
from conexao_bd import bd_conectar

def gerar_classificacao():
    """
        Função utilizada para gerar automaticamente a classificação do
        campeonato até o momento.
    """
    
    conexao = bd_conectar()
    cursor = conexao.cursor()
    
    # Comando utilizado para obter as informações da classificação:
    comando = """SELECT c.nome AS clube,
            SUM(CASE
                WHEN p.resultado_mandante > p.resultado_visitante AND
                p.id_mandante = c.id_clube THEN 3
                WHEN p.resultado_visitante > p.resultado_mandante AND
                p.id_visitante = c.id_clube THEN 3
                WHEN p.resultado_mandante = p.resultado_visitante THEN 1
                ELSE 0
            END) AS pontos,
            COUNT(p.id_partida) AS jogos,
            SUM(CASE
                WHEN (p.id_mandante = c.id_clube AND p.resultado_mandante >
                      p.resultado_visitante)  OR (p.id_visitante = c.id_clube
                      AND p.resultado_visitante > p.resultado_mandante) THEN 1
                ELSE 0
            END) AS vitorias,
            SUM(CASE
                WHEN p.resultado_mandante = p.resultado_visitante THEN 1
                ELSE 0
            END) AS empates,
            SUM(CASE
                WHEN (p.id_mandante = c.id_clube AND p.resultado_mandante <
                      p.resultado_visitante) OR (p.id_visitante = c.id_clube
                      AND p.resultado_visitante < p.resultado_mandante) THEN 1
                ELSE 0
            END) AS derrotas,
            SUM(CASE
                WHEN p.id_mandante = c.id_clube THEN p.resultado_mandante
                WHEN p.id_visitante = c.id_clube THEN p.resultado_visitante
                ELSE 0
            END) AS gols_pro,
            SUM(CASE
                WHEN p.id_mandante = c.id_clube THEN p.resultado_visitante
                WHEN p.id_visitante = c.id_clube THEN p.resultado_mandante
                ELSE 0
            END) AS gols_sofridos
            FROM clube c
            LEFT JOIN partida p ON c.id_clube IN (p.id_mandante,
            p.id_visitante) GROUP BY c.id_clube
            ORDER BY pontos DESC, vitorias DESC, c.nome"""
    
    try:
        cursor.execute(comando) # executa o respectivo comando
        classificacao = cursor.fetchall() # leitura do banco de dados

    except Error as e:
        print(f"Erro ao realizar a query: {e}")
        
    else:
        # Se a query anterior retornou algum resultado:
        if classificacao:
            # Imprime a classificação atual do campeonato:
            print("-" * 90)
            print(f"{'POS':^12}{'Clube':^30}{'J':^8}{'V':^8}{'E':^8}{'D':^8}{'SG':^8}{'PTS':^8}")
            print("-" * 90)
            pos = 1
            for clube in classificacao:
                sg = clube[6]-clube[7]
                print(f"{pos:^12}{clube[0]:^30}{clube[2]:^8}{clube[3]:^8}{clube[4]:^8}{clube[5]:^8}{sg:^8}{clube[1]:^8}")
                pos += 1
            print("-" * 90)
                
        else:
            print("A classificação não foi encontrada!\n")
        
    finally:
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

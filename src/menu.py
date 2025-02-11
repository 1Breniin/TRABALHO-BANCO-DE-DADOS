from time import sleep
from clube import clube_input, inserir_clube, remover_clube, buscar_clube, atualizar_clube
from jogador import jogador_input, inserir_jogador, remover_jogador, buscar_jogadores, atualizar_jogador
from partida import partida_input, inserir_partida, remover_partida, atualizar_partida, buscar_partidas
from estatisticas import maiores_artilheiros, mais_assistencias, mais_gols_acrescimos, maior_numero_cartoes, mais_estrangeiros
from exceptions import verifica_id


def menu_clubes():
    """Função utilizada para obter informações dos clubes."""
    
    executando = True
    # Enquanto o usuário quiser informações sobre os clubes:
    while executando:
        print("\n--------- MENU CLUBES ---------\n")
        
        print("1- Obter informações do clube")
        print("2- Adicionar um novo clube")
        print("3- Remover clube")
        print("4- Atualizar clube")
        print("5- Voltar\n")
        
        opcao = int(input("Opção selecionada: "))
        
        match opcao:
            case 1:
                nome = input("Qual clube deseja obter informações? ").strip().capitalize()
                buscar_clube(nome)
                         
            case 2:
                print("\nPreencha as informações do novo clube:\n")
                clube = clube_input()
                inserir_clube(clube)
                
            case 3:
                print("É preciso informar o ID do clube que deseja remover:")
                id_clube = verifica_id()
                remover_clube(id_clube)
        
            case 4:
                print("É preciso informar o ID do clube que deseja atualizar:")
                id_clube = verifica_id()
                atualizar_clube(id_clube)
                       
            case 5:
                executando = False
            
            case _:
                print("Opção inválida! Tente novamente...\n")
                sleep(1.5)


def menu_jogadores():
    """Função utilizada para obter informações dos jogadores."""
    
    executando = True
    # Enquanto o usuário quiser informações sobre os jogadores:
    while executando:
        print("\n--------- MENU JOGADORES ---------\n")
        
        print("1- Listar todos os jogadores do clube")
        print("2- Adicionar um novo jogador")
        print("3- Remover jogador")
        print("4- Atualizar jogador")
        print("5- Voltar\n")
        
        opcao = int(input("Opção selecionada: "))
        
        match opcao:
            case 1:
                nome_clube = input("Nome do clube: ").strip().capitalize()
                buscar_jogadores(nome_clube)
            
            case 2:
                print("\nPreencha as informações do novo jogador:\n")
                jogador = jogador_input()
                inserir_jogador(jogador)
                
            case 3:
                print("É preciso informar o ID do jogador que deseja remover:")
                id_jogador = verifica_id()
                remover_jogador(id_jogador)
        
            case 4:
                print("É preciso informar o ID do jogador que deseja atualizar:")
                id_jogador = verifica_id()
                atualizar_jogador(id_jogador)
                                      
            case 5:
                executando = False
            
            case _:
                print("Opção inválida! Tente novamente...\n")
                sleep(1.5)


def menu_partidas():
    """Função utilizada para obter informações das partidas."""
    
    executando = True
    # Enquanto o usuário quiser informações sobre as partidas:
    while executando:
        print("\n--------- MENU PARTIDAS ---------\n")
        
        print("1- Obter informações das partidas disputadas por um clube")
        print("2- Inserir uma nova partida")
        print("3- Remover partida")
        print("4- Atualizar partida")
        print("5- Voltar\n")
        
        opcao = int(input("Opção selecionada: "))
        
        match opcao:
            case 1:
                nome_clube = input("Nome do clube: ").strip().capitalize()
                buscar_partidas(nome_clube)
             
            case 2:
                print("\nPreencha as informações da nova partida:\n")
                partida = partida_input()
                inserir_partida(partida)
                
            case 3:
                print("É preciso informar o ID da partida que deseja remover:")
                id_partida = verifica_id()
                remover_partida(id_partida)
                
            case 4:
                print("É preciso informar o ID da partida que deseja atualizar:")
                id_partida = verifica_id()
                atualizar_partida(id_partida)
            
            case 5:
                executando = False
                
            case _:
                print("Opção inválida! Tente novamente...\n")
                sleep(1.5)
                

def menu_estatisticas():
    """Função utilizada para obter as estatísticas do campeonato."""
    
    executando = True
    # Enquanto o usuário quiser informações sobre as estatísticas:
    while executando:
        print("\n--------- MENU ESTATÍSTICAS ---------\n")
        
        print("1- Artilheiros do campeonato")
        print("2- Jogadores com mais assistências no campeonato")
        print("3- Clubes com mais gols nos acréscimos")
        print("4- Jogadores com mais cartões no campeonato")
        print("5- Clubes com mais jogadores estrangeiros do campeonato")
        print("6- Voltar\n")
        
        opcao = int(input("Opção selecionada: "))
        
        match opcao:
            case 1:
                maiores_artilheiros()
            
            case 2:
                mais_assistencias()
            
            case 3:
                mais_gols_acrescimos()
            
            case 4:
                maior_numero_cartoes()
            
            case 5:
                mais_estrangeiros()
                
            case 6:
                executando = False
                
            case _:
                print("Opção inválida! Tente novamente...\n")
                sleep(1.5)

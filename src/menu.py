from time import sleep
from clube import clube_input, inserir_clube, remover_clube, buscar_clube, atualizar_clube
from jogador import jogador_input, inserir_jogador, remover_jogador, buscar_jogadores, atualizar_jogador
from exceptions import verifica_id


def menu_clubes():
    """Função utilizada para obter informações dos clubes."""
    
    executando = True
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
                nome_clube = input("Nome do clube: ")
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
    
    pass


def menu_estatisticas():
    """Função utilizada para obter as estatísticas do campeonato."""
    
    executando = True
    while executando:
        print("\n--------- MENU ESTATÍSTICAS ---------\n")
        
        print("1- Artilheiros do campeonato")
        print("2- Jogadores com mais assistências no campeonato")
        print("3- Jogadores com mais gols e assistências no campeonato")
        print("4- Jogadores com mais cartões no campeonato")
        print("5- Voltar")
from time import sleep
from menu import menu_clubes, menu_jogadores, menu_partidas, menu_estatisticas


def executar():
    """Função utilizada para simular a execução do sistema."""
    
    executando = True
    while executando:
        print("\n=========== CAMPEONATO BRASILEIRO ===========\n")
        
        print("1- Classificação")
        print("2- Clubes")
        print("3- Jogadores")
        print("4- Partidas")
        print("5- Estatístiscas")
        print("0- Sair\n")
        
        opcao = int(input("Opção selecionada: "))
        
        match opcao:
            case 1:
                print("\n############## TABELA BRASILEIRÂO ##############\n")
            
            case 2:
                print("Informações sobre os clubes:\n")
                menu_clubes()
            
            case 3:
                print("Informações sobre os jogadores:\n")
                menu_jogadores()
                
            case 4:
                print("Partidas realizadas:\n")
                menu_partidas()
            
            case 5:
                print("Estatísticas do Campeonato\n")
                menu_estatisticas()
            
            case 0:
                executando = False
            
            case _:
                print("Opção inválida! Tente novamente...\n")
                sleep(1.5)
    
    
if __name__ == "__main__":
    executar()
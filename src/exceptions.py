def verifica_numero_camisa():
    """
        Função utilizada para verificar se o número da camisa digitado pelo
        usuário para um jogador é válido.
    """

    while True:
        try:
            numero_camisa = int(input("Número da Camisa: "))
    
        except ValueError:
            print("Tipo de dado inválido!\n")
    
        else:
            if numero_camisa >= 0:
                break
        
            else:
                print("Número da Camisa não permitido!\n")
    
    return numero_camisa


def verifica_altura():
    """
        Função utilizada para verificar se a altura digitada pelo
        usuário para um jogador é válido.
    """
    
    while True:
        try:
            altura = float(input("Altura (X.XX): "))
        
        except ValueError:
            print("Tipo de dado inválido!\n")
        
        else:
            if altura > 1.0 and altura < 2.50:
                break
        
            else:
                print("Altura não permitida!")
    
    return altura


def verifica_id():
    """
        Função utilizada para verificar se o id do clube digitado pelo
        usuário é válido.
    """
    
    while True:
        try:
            id = int(input("\tID: "))
        except ValueError:
            print("Valor inválido!")
        else:
            break
         
    return id


def verifica_resultado():
    """
        Função utilizada para verificar se o resultado da partida digitado pelo
        usuário é válido.
    """
    
    while True:
        try:
            resultado = int(input("\tResultado: "))
        except ValueError:
            print("Valor inválido!")
        else:
            if resultado >= 0:
                break
            
            else:
                print("Resultado não permitido!")
        
    return resultado


def verifica_minuto():
    """
        Função utilizada para verificar se o minuto do gol digitado pelo
        usuário é válido.
    """
    
    while True:
        try:
            minuto = int(input("\tMinuto: "))
        except ValueError:
            print("Valor inválido!")
        else:
            if minuto >= 0 and minuto < 110:
                break
            
            else:
                print("Minuto não permitido!")
         
    return minuto

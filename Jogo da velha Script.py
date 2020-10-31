def escolher_lado():
    jogador = 'Errado'
    
    while jogador not in ['X','O']:
        jogador = input('Jogador número 1: Quer jogar com X ou O?\n').upper()
            
        if jogador not in ['X','O']:
            print("Ops, esse não é uma entrada válida\n")
    
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

def mostrar_tab():
    
    print(f' {a} | {b} | {c}      (1) | (2) | (3) ')
    print('-----------    -----------------')
    print(f' {d} | {e} | {f}      (4) | (5) | (6) ')
    print('-----------    -----------------')
    print(f' {g} | {h} | {i}      (7) | (8) | (9) \n')
    
def jogada(njogador):
    
    indxJogada = ''
    digito = True
    foraRange = True
    ocupado = True
    
    while digito or foraRange or ocupado:
        indxJogada = input(f"Jogador número {njogador}, escolha onde deseja jogar: \n")
        
        if indxJogada.isdigit() == False:
            digito = True
            print("Ops, esse não é um dígito\n")
            continue
        else:
            digito = False

            if int(indxJogada) not in range(1,10):
                foraRange = True
                print("Ops, esse não é de 1-9\n")
            else:
                foraRange = False

            if int(indxJogada) in indxOcupados:
                ocupado = True
                print("Ops, esse local já está ocupado\n")
            else:
                ocupado = False
            
    indxOcupados.append(int(indxJogada))
    
    return int(indxJogada)

def atualizar_tab(indxJogada, jogador):
    
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global g
    global i
    
    
    if indxJogada == 1:
        a = jogador
    elif indxJogada == 2:
        b = jogador
    elif indxJogada == 3:
        c = jogador
    elif indxJogada == 4:
        d = jogador
    elif indxJogada == 5:
        e = jogador
    elif indxJogada == 6:
        f = jogador
    elif indxJogada == 7:
        g = jogador
    elif indxJogada == 8:
        h = jogador
    else:
        i = jogador
        
def ingame():
    
    lst = [a,b,c,d,e,f,g,h,i]
    
    global velha
    
    if a == b and a == c and a in ['X','O']:
        return True
    elif a == d and a == g and a in ['X','O']:
        return True
    elif a == e and a == i and a in ['X','O']:
        return True
    elif b == e and b == h and b in ['X','O']:
        return True
    elif c == f and c == i and c in ['X','O']:
        return True
    elif c == e and c == g and c in ['X','O']:
        return True
    elif d == e and d == f and d in ['X','O']:
        return True
    elif c == f and c == i and c in ['X','O']:
        return True
    elif g == h and g == i and g in ['X','O']:
        return True     
    elif lst.count(' ') == 0:
        velha = True
        return True
    else:
        return False
    
def rematch():
    
    resposta = 'Errada'
    
    while resposta not in ['S','N']:
        resposta = input('Deseja jogar outra partida? (S ou N)\n').upper()
        
        if resposta not in ['S','N']:
            print("Opa, reposta inválida\n")
        
    return resposta

print("Seja bem-vindo ao meu Jogo da Velha\n")

replay = 'S'

while replay == 'S':
    
    
    indxOcupados = []
    
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '
    
    jogador = escolher_lado()  
    
    mostrar_tab()
    
    njogador = '2'
    
    fimGame = False
    
    velha = False
    
    while fimGame == False:
        
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'

        if njogador == '1':
            njogador = '2'
        else:
            njogador = '1'
        
        indxJogada = jogada(njogador)
        
        atualizar_tab(indxJogada, jogador)

        mostrar_tab()
        
        fimGame = ingame()
        
    if velha:
        print("Velha :/")
    else:
        print(f"Parabéns o jogador {njogador} foi o vencedor! :)")

    replay = rematch()
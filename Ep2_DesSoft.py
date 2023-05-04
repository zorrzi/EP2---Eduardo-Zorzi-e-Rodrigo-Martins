#Exercicio 1

def define_posicoes(linha, coluna, orientacao, tamanho):

    lista = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            lista.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            lista.append([linha, coluna + i])

    return lista



#Exercicio 2

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    navio =define_posicoes(linha,coluna,orientacao,tamanho) 

    if nome_navio not in frota:
        frota[nome_navio] = [navio]
    else:
        frota[nome_navio].append(navio)

    return frota



#Exercicio 3

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


#Exercicio 4 

def posiciona_frota(frota):
    
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    
    
    
    for lista_navio in frota.values():
        for i in range(len(lista_navio)):
            for j in lista_navio[i]:
                grid[j[0]][j[1]] = 1

    return grid

#Exercicio 5

def afundados(frota, tabuleiro):

    soma = 0

    for lista_navios in frota.values():
        for i in range(len(lista_navios)):
            reset = 0
            for j in lista_navios[i]:
                if tabuleiro[j[0]][j[1]] == 'X':
                    reset +=1
                if reset == len(lista_navios[i]):
                    soma+=1

    return soma

#Exercico 6

def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for cord in range(len(navio)):
            if navio[cord][0] < 0 or navio[cord][0]>9 or navio[cord][1] < 0 or navio[cord][1]>9:
                return False

        

    for lista_navio in frota.values():
        for i in range(len(lista_navio)):
            for j in lista_navio[i]:
                if j in navio :
                    return False

    return True



# Exercicio 7:

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

i=0
while i<1:
    print ('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
    linha= int(input('Linha: '))
    coluna= int(input('Coluna: '))
    orientacao= input('[1] Vertical [2] Horizontal >')
    if orientacao == '1':
        orientacao = 'vertical'

    if posicao_valida(frota, linha, coluna, orientacao, 4) == True:
        frota = preenche_frota(frota, 'porta-aviões', linha, coluna, orientacao, 4)
        i += 1
    else:
        print ('Esta posição não está válida!')


i=0
while i<2:
    print ('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    linha= int(input('Linha: '))
    coluna= int(input('Coluna: '))
    orientacao= input('[1] Vertical [2] Horizontal >')
    if orientacao == '1':
        orientacao = 'vertical'

    if posicao_valida(frota, linha, coluna, orientacao, 3) == True:
        frota = preenche_frota(frota, 'navio-tanque', linha, coluna, orientacao, 3)
        i += 1
    else:
        print ('Esta posição não está válida!')

i=0
while i<3:
    print ('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    linha= int(input('Linha: '))
    coluna= int(input('Coluna: '))
    orientacao= input('[1] Vertical [2] Horizontal >')
    if orientacao == '1':
        orientacao = 'vertical'

    if posicao_valida(frota, linha, coluna, orientacao, 2) == True:
        frota = preenche_frota(frota, 'contratorpedeiro', linha, coluna, orientacao, 2)
        i += 1
    else:
        print ('Esta posição não está válida!')

i=0
while i<4:
    print ('Insira as informações referentes ao navio submarino que possui tamanho 1')
    linha= int(input('Linha: '))
    coluna= int(input('Coluna: '))
    if posicao_valida(frota, linha, coluna, 'vertical', 1) == True:
        frota = preenche_frota(frota, 'submarino', linha, coluna, orientacao, 1)
        i += 1
    else:
        print ('Esta posição não está válida!')


#Exercicio 8

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente= posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto




jogando = True
nova = [] 
while jogando == True:   #loop principal
    print (monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    repetida= True

    while repetida == True:
        linha= int(input('Jogador, qual linha deseja atacar? '))
        while linha > 9 or linha < 0:
            print('Linha inválida!')
            linha= int(input('Jogador, qual linha deseja atacar? '))

        coluna= int(input('jogador, qual coluna deseja atacar? '))
        while coluna >9 or coluna <0:
            print('Coluna inválida!')
            coluna= int(input('jogador, qual coluna deseja atacar? '))
        
        jogada= [linha,coluna]
        if jogada not in nova:
            nova.append(jogada)
            repetida = False
        else:
            print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente')

    tabuleiro_oponente= faz_jogada(tabuleiro_oponente,linha,coluna)  
    if afundados(frota_oponente,tabuleiro_oponente) == 10:
        jogando= False
        print('Parabéns! Você derrubou todos os navios do seu oponente!')

    

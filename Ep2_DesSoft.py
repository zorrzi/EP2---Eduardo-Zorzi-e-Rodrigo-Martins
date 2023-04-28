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
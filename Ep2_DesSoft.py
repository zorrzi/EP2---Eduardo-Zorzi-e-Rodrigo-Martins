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



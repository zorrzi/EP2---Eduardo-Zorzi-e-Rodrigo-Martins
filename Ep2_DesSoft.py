def define_posicoes(linha, coluna, orientacao, tamanho):

    lista = []

    if tamanho == 1:
        lista.append([linha, coluna])
    elif tamanho == 2:
        if orientacao == 'vertical':
            lista.append([linha,coluna])
            lista.append([linha + 1, coluna])
        else:
            if linha == 0 and coluna == 0:
                lista.append([linha,coluna])
                lista.append([linha,coluna + 1])
            else:
                lista.append([linha,coluna + 1])
                lista.append([linha,coluna + 2])
    elif tamanho == 3:
        if orientacao == 'vertical':
            lista.append([linha, coluna])
            lista.append([linha + 1, coluna])
            lista.append([linha + 2, coluna])
        else:
            if linha == 0 and coluna == 0:
                lista.append([linha, coluna])
                lista.append([linha, coluna + 1])
                lista.append([linha, coluna + 2])
            else:
                lista.append([linha, coluna +1])
                lista.append([linha, coluna +2])
                lista.append([linha, coluna +3])
    elif tamanho == 4:
        if orientacao == 'vertical':
            lista.append([linha, coluna])
            lista.append([linha + 1, coluna])
            lista.append([linha + 2, coluna])
            lista.append([linha + 3, coluna])
        else:
            if linha == 0 and coluna == 0:
                lista.append([linha, coluna])
                lista.append([linha, coluna + 1])
                lista.append([linha, coluna + 2])
                lista.append([linha, coluna + 3])
            else:
                lista.append([linha, coluna +1])
                lista.append([linha, coluna +2])
                lista.append([linha, coluna +3])
                lista.append([linha, coluna +4])

    return lista
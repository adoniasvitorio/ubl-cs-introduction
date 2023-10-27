import re


def main():
    assinatura = le_assinatura()
    textos = le_textos()
    numero_do_texto = avalia_textos(textos, assinatura)


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    return frase.split()


def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas


def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)


def compara_assinatura(as_a, as_b):
    list_diferenca = []
    for i in range(len(as_a)):
        diferenca = as_a[i] - as_b[i]
        diferencaAbs = abs(diferenca)
        list_diferenca.append(diferencaAbs)

    soma = sum(list_diferenca)
    grau_de_similaridade = soma / 6

    return grau_de_similaridade


def calcula_assinatura(texto):
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []

    for sentenca in separa_sentencas(texto):
        lista_sentencas.append(sentenca)

        for frase in separa_frases(sentenca):
            lista_frases.append(frase)

            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)

    tamanho_lista_sentencas = len(lista_sentencas)
    tamanho_lista_frases = len(lista_frases)
    tamanho_lista_palavras = len(lista_palavras)

    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    palavras_unicas = n_palavras_unicas(lista_palavras)

    tamanho_medio_de_palavra = tamanho_lista_palavras / len(lista_palavras)
    relacao_type_token = palavras_diferentes / tamanho_lista_palavras
    razao_hapax_legomana = palavras_unicas / tamanho_lista_palavras
    tamanho_medio_de_sentenca = len(texto) / tamanho_lista_sentencas
    complexidade_de_sentenca = tamanho_lista_frases / tamanho_lista_sentencas
    tamanho_medio_de_frase = len(texto) / tamanho_lista_frases

    as_b = [tamanho_medio_de_palavra, relacao_type_token, razao_hapax_legomana,
            tamanho_medio_de_sentenca, complexidade_de_sentenca, tamanho_medio_de_frase]

    return as_b


def avalia_textos(textos, ass_cp):
    lista = []
    for texto in textos:
        as_b = calcula_assinatura(texto)
        grau_similaridade = compara_assinatura(ass_cp, as_b)
        lista.append(grau_similaridade)

    index_menor_valor = lista.index(min(lista))
    numero_do_texto = index_menor_valor + 1

    return numero_do_texto

main()
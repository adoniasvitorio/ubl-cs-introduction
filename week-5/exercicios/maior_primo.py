"""
Exercicio 2
Escreva a função 'maior_primo' que recebe um número inteiro maior ou igual a 2 como parâmetro 
e devolve o maior número primo menor ou igual ao número passado à função
"""

def ePrimo (k):
    if (k <= 1):
        return False
    elif (k == 2):
        return True
    elif (k % 2 == 0):
        return False
    else:
        limite = int(k ** 0.5) + 1
        i = 3
        while (i < limite):
            if (k % i == 0):
                return False
            i += 2
        return True

def maior_primo (n):
    while (n >= 2):
        if (ePrimo(n)):
            primo = n
            return primo
        n -= 1

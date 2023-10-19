"""
Exercicio: Ler uma sequencia de numeros digitadas pelo usuario e, para cada número digitado, informar o seu fatorial.
"""

def fatorial(n):
    fatorial = 1
    while (n > 1):
        fatorial = fatorial * n
        n = n-1
    print(fatorial)


n = int(input("Digite um numero inteiro: "))
while (n >= 0):
    fatorial(n)
    n = int(input("Digite um numero inteiro: "))

"""
Exercicio Adicional 2
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima 'sim'; se não existir, imprima 'não'
"""
adjacentes  = False

numero = int(input("Digite um numero inteiro:"))
digito_anterior = numero % 10
numero //= 10

while (numero > 0 and not adjacentes):
    digito_atual = numero % 10
    numero //= 10

    if (digito_atual == digito_anterior):
        adjacentes = True

    digito_anterior = digito_atual

if (adjacentes):
    print("sim")
else:
    print("não")

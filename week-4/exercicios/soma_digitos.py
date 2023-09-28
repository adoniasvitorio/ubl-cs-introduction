"""
Exercicio 3
Escreva um programa que nreceba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.
"""
numero = int(input("Digite um número inteiro:"))
soma = 0

while (numero > 0):
    digito = numero % 10
    soma += digito
    numero //= 10
print(soma)

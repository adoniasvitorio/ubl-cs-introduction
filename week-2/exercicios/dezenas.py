"""
Exercicio 3
Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
Exemplo: Entrada 78615 | Saida 1
"""
numero = int(input("Digite um número inteiro:"))
dezenas = (numero //10) % 10
print('O dígito das dezenas é',dezenas)

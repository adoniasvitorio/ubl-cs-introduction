"""
Exercicio 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
calcule e imprima (saida de dados) seu perímetro e sua área.
"""
lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
perimetro = 4 * lado
area = lado ** 2
print('perímetro:', perimetro, '- área:', area)

"""
Exercicio 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritimetica.
"""

primeira_nota = int(input("Digitte a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota: "))
terceira_nota = int(input("Digite a terceira nota: "))
quarta_nota = int(input("Digite a quarta nota: "))

media = float((primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4)
print('A média aritmética é',media)

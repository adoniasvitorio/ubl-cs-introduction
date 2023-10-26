"""
Exercicio 01
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
"""

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura"))

linha = 1

while(linha <= altura):
    coluna = 1
    while(coluna <= largura):
        print("#", end="")
        coluna += 1
    print()
    linha += 1

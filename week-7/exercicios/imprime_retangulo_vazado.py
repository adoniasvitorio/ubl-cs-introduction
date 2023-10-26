"""
Exercicio 02
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
"""

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 1

while(linha <= altura):
    coluna = 1
    caracter = ""

    while(coluna <= largura):
        if((linha == 1) or (linha == altura)):
            caracter += "#"
        elif((coluna == 1) or (coluna == largura)):
            caracter += "#"
        else:
            caracter += " "
        coluna += 1
    print(caracter)
    linha += 1
        

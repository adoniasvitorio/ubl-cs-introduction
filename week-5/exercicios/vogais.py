"""
Exercicio 3
Escreva a função 'vogal' que recebe um único caractere como parâmetro e devolva ele como 'True' se ele for uma vogal e 'False' se for uma constante.
"""

def vogal (c):
    if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        return True
    if (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
        return True
    else:
        return False

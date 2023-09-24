"""
Exercicio 3
Receba um número inteiro na entrada e imprima 'Buzz' se o número for divisível por 5. Caso contrario, imprima o mesmo numero que foi dado na entrada.
"""
numero = int(input("Digite um número inteiro:"))
if(numero % 5 == 0):
    print("Buzz")
else:
    print(numero)

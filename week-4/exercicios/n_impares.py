"""
Exercicio 2
Receba um número inteiro positivo na entrada e imprima os n primeiros numeros impares naturais.
Para a saída, siga o formato do exemplo.
"""
n = int(input("Digite o valor de n: "))
impar = 0
num = 1

while (impar < n):
    if (num % 2 != 0):
        print(num)
        impar += 1
    num += 1

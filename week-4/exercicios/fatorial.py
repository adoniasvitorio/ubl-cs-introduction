"""
Exercicio 1
Excreva um programa que receba um número natural n na entrada e imprima n!(fatorial) na saída.
"""
n = int(input("Digite o valor de n: "))
fatorial = 1

if (n < 0):
    print("Não é possivel calcular o fatorial de um númeor negativo")
else:
    while (n > 0):
       fatorial *= n
       n -= 1
print(fatorial)

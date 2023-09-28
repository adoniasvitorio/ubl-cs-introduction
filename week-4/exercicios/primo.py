"""
Exercicio Adicional 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima 'primo'. Caso contrário, imprima 'não primo'.
"""
numero = int(input("Digite um número inteiro:"))

if (numero <= 1):
    print("não primo")
else:
    primo = True
    divisor = 2

    while (divisor <= (numero ** 0.5) and primo):
        if (numero % divisor == 0):
            primo = False
        divisor += 1
    if (primo):
        print("primo")
    else:
        print("não primo")

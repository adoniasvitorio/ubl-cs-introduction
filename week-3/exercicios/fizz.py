"""
Exercicio 2
Receba um número inteiro na entrada e imprima 'Fizz' se o númeor for divisível por 3. Caso contário o mesmo número que foi dado na entrada.
"""
numero = int(input("Digite um número inteiro:"))
if(numero % 3 == 0):
    print("Fizz")
else:
    print(numero)

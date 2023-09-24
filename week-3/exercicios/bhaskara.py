"""
Exercicio - Desafio da videoaula (Formula de Bhaskara)
Como pedido na videoaula desta semana, escreva um programa que calcula as raizes de uma equação do segundo grau.
O programa deve receber os parâmetros a, b e c da equação ax2 + bx + c, respectivamente, e imprimir o resultado da saída seguinte maneira:
Quando não houver raízes imprima 'esta equação não possui raízes reais'.
Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidades 2) imprima 'a raiz desta equacao e x'.
ou a raiz dupla desta equação e x, onde x é o valor da raiz dupla.
Quando houver duas raízes reais imprima 'as raízes da equação são X e Y onde X e Y são os valores das raízes.
Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente 
"""

a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

delta = (b**2) - (4*a*c)

if (delta < 0):
    print("esta equação não possui raízes reais")
else:
    if (delta == 0):
        raiz = -b / (2*a)
        print("a raiz desta equação é", raiz)
    else:
        raiz1 = (-b + (delta**0.5)) / (2*a)
        raiz2 = (-b + (delta**0.5)) / (2*a)

        if (raiz1 == raiz2):
            print("a raiz dupla desta equação é", raiz1)
        else:
            if (raiz1 < raiz2):
                print("as raízes desta equação são", raiz1,"e", raiz2)
            else:
                print("as raízes desta equação são", raiz2, "e", raiz1)

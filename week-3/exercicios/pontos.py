"""
Exercicio - Distancia entre dois pontos
Receba 4 numeros na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, as coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, as coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distancia entre os dois pontos. Se a distância for maior ou igual a 10, imprima 'longe' na saida. Caso contrario, quando a distancia for menor que 10, imprima 'perto'.
"""
x1 = float(input("Digite a coordenada x do primeiro ponto:"))
y1 = float(input("Digite a coordenada y do primeiro ponto:"))

x2 = float(input("Digite a coordenada x do segundo ponto:"))
y2 = float(input("Digite a coordenada y do segundo ponto:"))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if (distancia >= 10):
    print("longe")
else:
    print("perto")

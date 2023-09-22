"""
Exercicio 4
Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que,
dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. 
A saida deve estar no formato a dias, b horas, c minutos e d segundos.
"""
input_segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = input_segundos // 86400
rSegundos = input_segundos % 86400
horas = rSegundos // 3600
rSegundos %= 3600
minutos = rSegundos // 60
segundos = rSegundos % 60

print(dias,'dias,',horas,'horas,',minutos,'minutos e',segundos,'segundos.')

"""
Exercirio 3
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem.

Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 esta fechada.
"""
nome = input("Digite o nome do cliente:")
dia = input("Digite o dia de vencimento:")
mes = input("Digite o mês de vencimento:")
valor = input("Digite o valor da fatura:")

print('Olá,', nome)
print('A sua fatura com vencimento em', dia, 'de', mes, 'no valor de R$',valor,'está fechada.')

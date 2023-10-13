"""
Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.
Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

* Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
* Caso contrário, o computador toma a iniciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

"""
def computador_escolhe_jogada(n, m):
    jogada_computador = 1
    while (jogada_computador != m):
        if ((n - jogada_computador) % (m + 1) == 0):
            return jogada_computador
        else:
            jogada_computador += 1
    return jogada_computador

def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while (not jogada_valida):
        jogada_usuario = int(input("Quantas peças você vai tirar? "))
        if (jogada_usuario > m or jogada_usuario < 1):
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogada_valida = True
    return jogada_usuario

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    computador_inicia = False

    if (n % (m + 1) == 0):
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        computador_inicia = True
        
    while (n > 0):
        if (computador_inicia):
            computador_remove = computador_escolhe_jogada(n, m)
            n -= computador_remove

            if (computador_remove == 1):
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", computador_remove, "peças")
            computador_inicia = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n -= jogador_remove

            if (jogador_remove == 1):
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogador_remove, "peças")
            computador_inicia = True

        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if (n != 0):
                print("Agora restam,", n, "peças no tabuleiro.")
                print()
    print("Fim do jogo! O Computador ganhou!")

def campeonato():
    rodada = 1

    while (rodada <= 3):
        print()
        print("**** Rodada", rodada, "****")
        print()

        partida()
        rodada += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()

    print("1 - para uma partida isolada")
    print("2 - para um campeonato")

    escolhe_partida = int(input())

    if (escolhe_partida == 1):
        print()
        print("Você escolheu uma partida!")
        print()
        partida()
    else:
        print()
        print("Você escolheu campeonato!")
        print()
        campeonato()

main()

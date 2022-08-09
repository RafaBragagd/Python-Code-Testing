import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    '''Variaveis globais'''
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    '''Menu de niveis'''
    print("Qual nível de dificuldade?")
    print("|--------------|-----------|")
    print("|   Facil      |     1     |")
    print("|   Médio      |     2     |")
    print("|  Dificil     |     3     |")
    print("|______________|___________|")
    nivel = int(input("Defina Nivel: "))

    '''Define o nivel selecionado'''
    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    '''Laço de repetição do jogo'''
    for rodada in range(1, tentativas + 1):
        '''Valor digitado pelo usuario'''
        print("Rodada {} de {}".format(rodada, tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!\n \n")
            continue

        '''Testes logicos que irão dizer se o usuario acertou
        e se caso errar se é maior que o numero secreto'''
        acertou = (numero_secreto == chute)
        maior   = (numero_secreto <  chute)

        '''Ifs realizando os testes logicos'''
        if (acertou):
            print(f"Parabens, Você acertou e fez {pontos} pontos!!")
            break
        else:
            if (maior):
                print("Você errou!! Seu numero é maior que o número secreto \n")
            else:
                print("Você errou!! Seu numero é menor que o número secreto \n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if (rodada >= tentativas):
            print("O valor era {}".format(numero_secreto))
    '''Exibe a tela de encerramento do jogo'''
    print("************************************")
    print("************Fim de Jogo*************")
    print("************************************\n")

if (__name__ == "__main__"):
    jogar()
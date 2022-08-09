import random








def jogar():
    '''Imprime mensagem inicial'''
    mensagem_abertura()

    '''Puxa uma palavra aleatoria'''
    palavra_secreta = aleatorizado_palavra()

    '''criando a lista com as letras ocultas'''
    letras_acertadas = Inicializa_letra_acertadas(palavra_secreta)


    '''Variaveis globais'''
    enforcou = False
    acertou = False
    erros = 0


    '''loop do jogo'''
    while(not enforcou and not acertou):

        '''Imprime forca formatada'''
        print(f"Você possui {7 - erros} tentativas: ", end="")
        forca_formatada(letras_acertadas)

        '''Realiza a captura e analise das letras digitadas pelo
        usuario'''
        chute = (input("Qual letra? ")).strip().upper()

        if(chute in palavra_secreta):
            letras_acertadas = marcacao_das_letras(chute, palavra_secreta, letras_acertadas)
        else:
            erros = erros + 1

        '''Atualiza os criterios do loop do jogo'''
        desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    '''Realiza uma mensagem de acordo com o resultado'''
    if acertou:
        print("Parabens você ganhou!!!")
    else:
        print("Você perdeu :(")
    print(f"A palavra era: {palavra_secreta}.\n")

def mensagem_abertura():
    print("*********************************")
    print("**Bem vindo ao jogo de Forca!!!**")
    print("*********************************")

def aleatorizado_palavra():
    '''abrindo o arquivo de palavras'''
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    '''Aleaotorizando uma palavra e colocando na palavra chave'''
    num = random.randrange(0, len(palavras))
    palavra_secreta = (palavras[num]).upper()
    return palavra_secreta

def Inicializa_letra_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def marcacao_das_letras(chute, palavra_secreta, letras_acertadas):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute
        index = index + 1
    return letras_acertadas

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

def forca_formatada(letras_acertadas):
    for indice in letras_acertadas:
        print(f" {indice} ", end="")
    print("")

if (__name__ == "__main__"):
    jogar()
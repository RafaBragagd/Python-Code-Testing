import forca
import adivinhacao


print("*********************************")
print("******Escolha o seu Jogo!!!******")
print("*********************************")

'''Menu de jogos'''
print("Qual o seu jogo?")
print(" __________________________ ")
print("|   Forca      |     1     |")
print("|--------------|-----------|")
print("| Adivinhação  |     2     |")
print("|______________|___________|")
jogo = int(input("Defina o jogo: "))

if (jogo == 1):
    print("Jogando forca!!!")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação!!!")
    adivinhacao.jogar()
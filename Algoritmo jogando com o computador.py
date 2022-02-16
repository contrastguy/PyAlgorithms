from random import randint
contador = 0
num = randint(0,10)
acerto = False
contador = 0
while not acerto :
    jogador= int(input("Digite o número que você acha que eu pensei:  "))
    if jogador != num:
        print("Você errou !".format(num))
        print("====Tente novamente====")
        contador +=1
    else:
        acerto = True
        contador+=1
print("Parabéns você acertou! Você teve que adivinhar {} vezes até acertar".format(contador))

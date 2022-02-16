import random

print(f"{' Jogo do Jokenpô ':=^50}")
print ("""Opções de Escolha
[1] Pedra
[2] Papel
[3] Tesoura""")
jogador =int(input("Faça sua escolha: "))
print(f'{" Jokenpô! ":=^50}')
computador =random.choice(["Pedra","Papel","Tesoura"])
print("Escolha do computador : \033[33m{}\033[m".format(computador))
if computador == "Pedra":
    if jogador == 1:
        print("Empate!")
    elif jogador ==  2:
        print("Você venceu!")
    elif jogador ==  3:
        print("Você perdeu!")
    else:
        print("Opção inválida! Tente novamente.")
elif computador == "Papel":
    if jogador == 1:
        print("Você perdeu!")
    elif jogador == 2:
        print("Empate!")
    elif jogador == 3:
        print("Você ganhou!")
    else:
        print("Opção inválida! Tente novamente.")
elif computador == "Tesoura" :
    if jogador == 1:
        print("Você ganhou!")
    elif jogador == 2:
        print("Você perdeu!")
    elif jogador == 3:
        print("Empate!")
    else:
        print("Opção inválida! Tente novamente.")

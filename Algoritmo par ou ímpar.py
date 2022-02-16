from random import randint
contador = 0
escolha=" "
while escolha not in "PI" :
    escolha = str(input("Par ou Ímpar? [P/I] ")).upper()
while True:
    jogador = int(input("digite um número: "))
    computador  = randint(0,11)
    print(f"O Computador colocou {computador}, e você colocou {jogador}.")
    print("----------------")
    soma = jogador + computador
    if (soma%2) == 0 and escolha == "P":
        contador += 1
        print(f"Você venceu! Com um total de {contador} vitórias.  ")
    if (soma%2) != 0  and escolha == "P":
        print(f"Você perdeu! Com um total de {contador} vitórias.")
        break
    if (soma%2) == 0  and escolha == "I":
        print(f"Você perdeu! Com um total de {contador} vitórias.")
        break
    if (soma%2) != 0  and escolha == "I":
        contador += 1
        print(f"Você venceu! Com um total de {contador} vitórias.  ")
print("--Fim do jogo--")

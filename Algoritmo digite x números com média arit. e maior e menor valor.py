import time
num = 0
flag = "Ss"
contador = 0
média = 0
maiorv=0
menorv=0
while flag in "Ss" :
    num=int(input("Digite aqui um número: "))
    print(num)
    contador+=1
    média += num
    if contador == 1:
        menorv = maiorv = num
    else:
        if num>maiorv:
            maiorv=num
        if num<menorv:
            menorv=num
    flag = str(input("Quer continuar? [S/N] :  ")).upper()
médiaarit = média/contador
print("==========")
print("Finalizando...")
time.sleep(5)
print("Fim. Você digitou {} números.".format(contador))
print("A média aritmética dos números digitados é {}".format(médiaarit))
print("O maior valor entre eles é {}".format(maiorv))
print("O menor valor entre eles é {}".format(menorv))

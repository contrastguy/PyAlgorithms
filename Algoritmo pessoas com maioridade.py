anoatual = 2021
maiorida = 0
menorida = 0

for i in range(1,8):
    idade = int(input("Digite aqui o ano de nascimento da {}ª pessoa :".format(i)))
    resultado = anoatual - idade
    print(idade)
    if resultado >= 18:
        maiorida+=1
    else:
        menorida+=1

print("O número de pessoas maiores de idade é : {}".format(maiorida))
print("O número de pessoas menores de idade é : {}".format(menorida))

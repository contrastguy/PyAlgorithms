idade= 0
sexo=" "
maiori=0
homem=0
mulher=0
while  True:
    idade = int(input("Digite aqui sua idade: "))
    if idade >= 18:
        maiori+=1
    sexo=" "
    while sexo not in "MF":
        sexo= str(input("Digite aqui seu Sexo [M/F]: ")).upper()
    if sexo =="M":
        homem+=1
    if sexo =="F" and idade < 20:
        mulher+=1
    flag=" "
    while flag not in "SN":
        flag=str(input("Quer continuar? [S/N]  ")).upper()
    if flag=="N":
        break

print("Fim do programa.")
print(f"Foram cadastrados {maiori} maiores de 18 anos.")
print(f"Foram cadastrados {homem} homem(s).")
print(f"Foram cadastradas {mulher} mulheres que tem menos de 20 anos.")

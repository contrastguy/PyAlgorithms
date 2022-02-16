média = 0
contador = 0
masculino = "M"
feminino = "F"
maiori  = 0
nomehomemvelho=" "
for m in range(1,5):
    print(f'{" {}ª pessoa ":=^20}'.format(m))
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO: "))
    média += idade
    if sexo in"Mmmasculino":
        if m == 1:
            maiori = idade
            nomehomemvelho = nome
        if idade>maiori and sexo in"Mmmasculino" :
            maiori = idade
            nomehomemvelho = nome

if  sexo in "Fffeminino":
    if idade < 20:
        contador+=1
    else:
        contador = 0
médiaarit = média / 4
print("============")
print("A média das idades do grupo é {}, e a soma das idades é {}".format(médiaarit,média))
print("A idade do homem mais velho é {} e se chama {}".format(maiori,nomehomemvelho))
print("O número de mulheres com menos de 20 anos é : {}".format(contador))

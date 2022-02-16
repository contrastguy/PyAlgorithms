
maiorp=0
menorp=0
for i in range(1,6):
    peso = float(input("Digite aqui o peso da {}ª pessoa : ".format(i)))
    print(peso)
    if i == 1 :
        maiorp=peso
        menorp=peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso

print("O maior peso é : {}kg".format(maiorp))
print("O menor peso é : {}kg".format(menorp))

import math
catop = float(input("digite aqui o valor do cateto oposto:"))
catadj = float(input("Digite aqui o valor do cateto adjacente:"))
hipotenusa = math.pow(catop,2) +  math.pow(catadj,2)
thunder = math.sqrt(hipotenusa)

print("A \033[36;40mhipotenusa\033[m é : {}".format(thunder))

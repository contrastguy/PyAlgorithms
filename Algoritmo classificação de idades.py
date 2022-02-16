idade = int(input("Digite aqui o seu ano de nascimento: "))
anoatual = 2021

if  (anoatual - idade) <= 9:
    print("Mirim")
elif 9 < (anoatual - idade) <= 14 :
    print("Infantil")
elif 14 < (anoatual - idade) <= 19 :
    print("Júnior")
elif 19 < (anoatual - idade) <= 20:
    print("Sênior")
elif 20 < (anoatual - idade) :
    print("Master")

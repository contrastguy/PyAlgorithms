ano = int(input("Digite aqui o seu ano de nascimento : "))
anoatual = 2021
if (anoatual - ano == 18):
   print("Em 2021 , quem nasceu em {}, tem 18 anos.\n Você tem que se alistar \033[35m imediatamente!\033[m".format(ano))
elif (anoatual - ano > 18):
    print("Em 2021 , quem nasceu em {}, tem mais de 18 anos e já passou da hora de se alistar!".format(ano))
    print(" ",(anoatual - ano) - 18 , "ano(s) é o tempo que já passou do ano do seu alistamento")
else:
    print("em 2021, quem nasceu em {}, tem menos de 18 anos e ainda não chegou a hora de se alistar!" .format(ano) )
    print(" ", 18 - (anoatual - ano ), "ano(s) é o que falta para chegar ao seu ano(s) de alistamento")

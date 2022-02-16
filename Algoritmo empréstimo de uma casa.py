valorcasa  = int(input("Digite aqui o valor da casa:"))
saláriocomprador = int(input("Digite aqui o seu salário:"))
meses = int(input("Digite aqui em quanto tempo você vai pagar :"))

prestaçãomensal = valorcasa // meses


if prestaçãomensal > (saláriocomprador * 0.30):
  print("Infelizmente você \033[35m não poderá \033[m comprar esta casa , pois a prestação mensal\033[32m excedeu 30% do seu salário\033[m,\n como está escrito aqui:{} ".format(prestaçãomensal))
elif prestaçãomensal == saláriocomprador:
    print("O valor da prestação mensal é\033[35m igual\033[m ao salário do comprador")
else:
  print("Você \033[34m pode \033[m comprar esta casa! A prestação mensal vai ser : {}".format(prestaçãomensal))

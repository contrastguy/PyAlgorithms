peso = float(input("Digite o seu peso (em kilos):  "))
altura =  float(input("Digite aqui sua altura (coloque o ponto):  "))

imc= peso/(altura**2)

if imc < 18.5:
    print("Você está \033[36mabaixo do peso\033[m")
elif  18.5 <= imc < 25:
    print("Você está com \033[36mPeso ideal\033[m")
elif 25 <=  imc < 30 :
    print("Você está com \033[36mSobrepeso\033[m ")
elif 30 <= imc < 40:
    print("Você está com \033[36mobesidade\033[m ")
elif 40 <= imc:
    print("Você está com \033[36mobesidade mórbida\033[m ")

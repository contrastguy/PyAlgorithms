masculino = "M"
feminino = "F"
s =""
while s != masculino and feminino:
    s = str(input("Digite aqui o seu sexo :  ")).upper()
    print(s)
    if s != masculino and feminino:
        print("Digite novamente.")
print("Fim")

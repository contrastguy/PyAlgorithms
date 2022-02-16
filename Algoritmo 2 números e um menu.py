import time

a = float(input("Digite aqui um número: "))
b = float(input("Digite aqui outro número: "))
final = 0
escolha = 0
print("====Menu====")
print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
print("========")

while escolha != 5:
    escolha = int(input("Escolha dentre um dos números do menu, para executar ações: "))
    if escolha == 1:
        final =  a+b
        print("========")
        print(final)
        print("========")
    elif escolha == 2 :
        final= a*b
        print("========")
        print(final)
        print("========")
    elif escolha == 3:
        if a>b:
            print("========")
            print("Entre os números escolhidos, o maior é : {}".format(a))
            print("========")
        else:
            print("========")
            print("Entre os números escolhidos , o maior é : {}".format(b))
            print("========")
    elif escolha == 4:
        print("========")
        a = float(input("Digite aqui um número: "))
        b = float(input("Digite aqui outro número: "))
        print("========")
    elif escolha == 5 :
        print("========")
        print("Terminando...")
        time.sleep(3)
    else:
        print("========")
        print("Opção inválida, tente novamente.")
        print("========")
print("Fim do programa")

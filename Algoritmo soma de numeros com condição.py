soma=0 #acumulador
for i in range(0,6):
    num = int(input("Digite aqui um número: "))
    if (num%2)== 0 :
        soma = soma + num #acumulação: 0 + num = soma , x + num = soma e assim vai 
print(f'{" Fim " :=^40}')
print("A soma dos valores que são pares é : {} ".format(soma))

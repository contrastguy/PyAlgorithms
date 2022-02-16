tupla = ( "zero","um", "dois" ,"três", "quatro", "cinco", "seis", "sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
num=int(input("Digite um número entre 0 e 20: "))
if num not in range(0,len(tupla)):
    print("Tente novamente")
    num=int(input("Digite um número entre 0 e 20: "))
else:
    print(f"Você digitou o número {tupla[num]}")    

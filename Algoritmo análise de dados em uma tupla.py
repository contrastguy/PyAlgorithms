n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
n3=int(input("Digite um número: "))
n4=int(input("Digite um número: "))

tupla= (n1,n2,n3,n4)
print(f"Você digitou os valores {tupla}")
print(f"Aparece {tupla.count(9)} vez(es) o número 9 na tupla")
print(f"O primeiro valor de 3 foi encontrado na posição {tupla.index(3)}")
contador=0
for i in tupla : #para cada índice da tupla , veja se tem um valor par e depois usa o contadopr para contar
    if i % 2 == 0 :
        contador+=1
print(f"Tem {contador} números pares ")

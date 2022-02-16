print(f'{" O número é primo ou não?":=^50}')
print("\033[32m Obs:O número que for primo , não pode ser divisível por mais de 2 números \033[m")
a = int(input("Digite aqui um número: "))
totdivisores=0
for i in range(1, a+1):
    if (a%i)==0:
        print( "\033[33m")
        totdivisores+=1
    else:
        print("\033[32m" )
    print(i , end=" ")
print("O total de divisores é: {}".format(totdivisores))
if totdivisores==2:
    print("O número é primo")
else:
    print("O número não é primo")

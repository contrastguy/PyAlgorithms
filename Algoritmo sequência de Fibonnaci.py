n1 = 0  #a sequência já começa com esses 2 números como base
n2 = 1
seq = int(input("Digite aqui quantos números você quer ver na sequência: "))

contador = 3  #tem que começar a partir do n3 poque o 0 e 1 já estão inclusos e contados

print("{} , {}".format(n1,n2) ,end=" ")  #início da sequência , só pra colocar os números base e o resto deixa com o n3
while contador < seq:
    n3  = n1 + n2
    print(", {} ".format(n3), end=" ") 
    contador+=1
    n1=n2     #transposição dos números
    n2=n3
print("Fim")

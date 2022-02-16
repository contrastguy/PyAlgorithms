#Programa de criação de um número fatorial

contador=int(input("digite o número aqui:"))
fatorial = contador
homem = 1
while (contador-homem) > 1:
   fatorial = fatorial*(contador-homem)
   homem+=1

print("resultado do \033[33mnúmero fatorial\033[m:{}" .format(fatorial))

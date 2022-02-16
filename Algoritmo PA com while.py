import time

termo1 = int(input("Digite o primeiro termo: "))
razão =  int(input("Digite aqui a razão: "))
contador = 0
termos = 0

while contador<10:
    termo1= termo1*razão
    contador+=1
    print(termo1)
print("Finalizando...")
time.sleep(5)
print("Fim da PA de {} termos.".format(contador))
print("==================================")
termos = int(input("Você quer ver mais termos? Quantos?   "))
while termos != 0:
    termo1= termo1*razão
    termos-=1
    print(termo1)
print("Finalizando...")
time.sleep(5)
print("Fim da PA")
print("==================================")

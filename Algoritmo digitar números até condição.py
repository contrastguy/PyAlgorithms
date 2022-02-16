contador = 0
num = 0
num =int(input("Digite aqui um número: "))
soma=0

while num != 999 :
    num =int(input("Digite aqui um número: "))
    contador += 1
    soma += num
print("=====")
print("Fim")
print("=====")
print("Você digitou números {} vezes. E a soma entre eles é {}".format(contador,soma-999))

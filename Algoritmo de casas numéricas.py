número = str(input("Digite aqui um número : "))
núm = int(número)
#pega o número , divide por 10 e o resto é a unidade 
u = núm %10
d = núm //10 %10
c = núm //100 % 10
m = núm //1000 %10

print("unidade:{}".format(u))
print("dezena:{}".format(d))
print("centena:{}".format(c))
print("milhar:{}".format(m))

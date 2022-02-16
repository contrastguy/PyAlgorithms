
f=  str(input("Digite aqui sua frase: "))
lf = len(f)
m = f.strip()[::-1]
print("O reverso da frase é : {}".format(m))
total=0
for i in (0,f):
    if f == m:
        total=+1
    else:
        total=0
if total != 0:
        print("A frase é palíndroma")
else:
    print("A frase não é palíndroma")

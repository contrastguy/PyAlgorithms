tupla =("Bolo",14.50,
"Laranja",3.50,
"Requeijão",9,
"Sorvete",20,
"Banana",8.50,
"Sabonete",4.50,
"Refrigerante",9.90)
for i in range(0,len(tupla)):
    if i %2 ==0:
        print(tupla[i],end="...........")
    else:
        print("%.2f" % tupla[i])

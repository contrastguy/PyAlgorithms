print("-"*20)
print("  CAIXA ELETRÔNICO  ")
print("-"*20)
valor = int(input("Digite aqui o valor de saque: R$ "))
total=valor
céd=50
totcéd=0
while True:
    if total>=céd:
        total-=céd
        totcéd+=1
    else:
        if totcéd>0:
            print(f"Será sacado {totcéd}cédulas de {céd}")
        if céd==50:
            céd=20
        if céd==20:
            céd=10
        if céd==10:
            céd=1
        totcéd=0
        if total == 0: #Se o total não zerar, ele volta lá para o início da condição if total>=céd
            break
print("FIM . VOLTE SEMPRE!")

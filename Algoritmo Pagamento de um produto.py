print(f'{" Loja do Matheus ":=^40}')
valor = float(input("Digite aqui o preço das compras: "))
print("""Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] parcelado em 2x no cartão
[4] parcelado em 3x ou mais no cartão""")
escolha = int(input("Escolha a forma de pagamento:  "))
if escolha == 1:
    print("Pagamento à vista dinheiro/cheque")
    final = valor - (valor*0.10)
    print("O valor de R${} , será R${}.".format(valor,final))
elif escolha == 2:
    print("Pagamento à vista cartão")
    final = valor -(valor*0.05)
    print("O valor de R${}, será de R${}".format(valor,final))
elif escolha == 3:
    print("Pagamento parcelado em 2x no cartão")
    parcelas = valor/2
    print("O valor das parcelas será: R${}".format(parcelas))
elif escolha == 4:
    print("Pagamento parcelado em 3x ou mais no cartão")
    total = valor + (valor*0.20)
    parcelas = int(input("Quantas parcelas você vai pagar ? "))
    final = total/parcelas
    print("O valor das parcelas será de R${}".format(final))
    print("O total será {}parcelas de R${}, e o valor final com juros é R${}.".format(parcelas,final,total))
else:
    print("OPÇÃO INVÁLIDA. Tente outra forma de pagamento.")

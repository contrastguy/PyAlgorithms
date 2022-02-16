while True:
    num = int(input("Você quer ver a tabuada de qual valor?  "))
    if num < 0:
        break
    print("=" * 20)
    for c in range(1,11):
        print(f"{num}x{c}={num*c}")
    print("=" *20)
print("Fim do programa , porque você digitou um número negativo.")    

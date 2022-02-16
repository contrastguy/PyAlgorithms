print(f'{" PA de 10 termos ":=^50}')
primeirotermo = float(input("Digite aqui o primeiro da PA: "))
razão = float(input("Digite aqui a razão da PA: "))

for i in range(0,9):
    primeirotermo = primeirotermo + razão
    print(primeirotermo)
print("Fim")
 

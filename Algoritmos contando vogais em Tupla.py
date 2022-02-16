def Check_vog(tupla,vogais):
    final=[each for each in tupla if each if each in vogais]
    print(final)
tupla=("carro", "laranja","youtube","cenoura","jacare","garsa","joao")
vogais= "AaEeIiOoUu"

for i in range(0,len(tupla)):
        print(f"A palavra {tupla[i]} tem as vogais")
        Check_vog(tupla[i],vogais);

nome = str(input("Digite aqui seu nome completo:"))
titulo = nome.strip().title()
final = "Silva" in titulo
print("Seu nome tem \033[32mSilva\033[m? : {}".format(final))

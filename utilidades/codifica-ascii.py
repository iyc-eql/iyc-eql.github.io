frase = input("Escribe una frase: ")
for caracter in frase:
    ascii = ord(caracter)
    print(f"{ascii}", end=" ")

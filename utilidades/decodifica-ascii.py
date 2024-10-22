frase = input("Escribe una frase codificada en ASCII (secuencia de números decimales): ")
frase = frase.split(" ")
caracteres = []
for ascii in frase:
    caracter = chr(int(ascii))
    caracteres.append(caracter)
print("".join(caracteres), end="")
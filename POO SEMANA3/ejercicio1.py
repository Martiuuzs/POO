valor = input("Ingrese un mensaje: ")
crypto = ""
for letra in valor:
    if not letra.isalpha():
        continue
    #print(letra)
    #se encarga de sumarle una letra mas a la letra actual, por ejemplo: si A + 1 = B
    letra = letra.upper()
    codigoAscii = ord(letra) + 1
    if codigoAscii > ord("Z"):
        codigoAscii = ord("A")
    crypto += chr(codigoAscii)
print(crypto)

#SI MANDAMOS UNA LETRA, POR EJEMPLO: "A" + 1, NOS DEVOLVERÍA "B"
texto = input("Ingrese un texto: ")
palabras = texto.split(" ")
for i, palabra in enumerate(palabras):
    print("Palabra Nro " + str(i) + " " + palabra)
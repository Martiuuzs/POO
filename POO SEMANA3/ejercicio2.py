valNumeros = input("Ingrese una lista de numeros: ")
listaNumeros = valNumeros.split(" ")
print(listaNumeros)
suma = 0
try:
    for numero in listaNumeros:
        suma += float(numero)
    print("La suma de la lista es: " + str(suma))
    print("Cantidad de numeros: " + str(len(listaNumeros)))
    print("Cantidad de caracteres: " + str(len(valNumeros)))
except:
    print("Un valor de la lista no es numerico")
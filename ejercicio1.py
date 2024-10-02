try:
    numero = float(input("Ingrese un numero: "))
    if numero % 2 == 0:
        numero_par = "El numero ingresado es PAR"

    else:
        numero_par = "El numero ingresado es IMPAR"

    print(numero)
    print(numero_par)

except:
    print("Error, ingrese solo números.")
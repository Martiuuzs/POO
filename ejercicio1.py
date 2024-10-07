try:
    numero = float(input("Ingrese un numero: "))
    if numero % 2 == 0:
        numero_par = "El numero ingresado es PAR"
        print(numero_par)



    else:
        numero_impar = "El numero ingresado es IMPAR"
        print(numero_impar)



except:
    print("Error, ingrese solo números.")
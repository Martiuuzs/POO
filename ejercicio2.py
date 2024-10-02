while(True):
    try:
        num1 = float(input("Enter first number: "))
        num2  = float(input("Enter second number: "))
        if num1 > 20:
            print("Ingrese un valor del 0 al 20")
            break
        elif num2 > 20:
            print("Ingrese un valor del 0 al 20")
            break
        promedio = (num1 * 0.6) +  (num2 * 0.4)
        estado = "Alumno  desaprobado"
        if num1 > 20:
            print("Ingrese un valor del 0 al 20")
            break
        elif num2 > 20:
            print("Ingrese un valor del 0 al 20")
            break
        if  promedio > 10:
            estado  = "Alumno aprobado"
            print(estado)
    
    except:
        print("Error, por favor ingrese un valor numerico")
    else:
        print("OK")
        break






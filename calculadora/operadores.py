def suma(n1, n2):
    try:
        resultado =  int(n1) + int(n2)
    except ValueError:
        print("Ingrese solo numeros")
    else:
        return resultado
    
def resta(n1, n2):
    try:
        resultado =  int(n1) - int(n2)
    except ValueError:
        print("Ingrese solo numeros")
    else:
        return resultado
    
def multiplicacion(n1, n2):
    try:
        resultado =  int(n1) * int(n2)
    except ValueError:
        print("Ingrese solo numeros")
    else:
        return resultado
    
def division(n1, n2):
    try:
        resultado =  int(n1) / int(n2)
    except ValueError:
        print("Ingrese solo numeros")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        return resultado

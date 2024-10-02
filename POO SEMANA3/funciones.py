"""mensaje = input("Ingrese un mensaje: ")
print(mensaje.upper())
print(mensaje.lower())
print(mensaje.capitalize())
letra = input("Ingrese una letra: ")
#reconoce si el valor ingresado es un numero o una letra
if letra.isalpha():
    print("Caracter alfabetico")
    #ord no da el codigo aski del valor ingresado
    print(ord(letra))
    #nos da la letra del codigo aski
    print(chr(ord(letra)))
else:
    print("Caracter NO alfabetico")
print(ord(letra))
codigoAsccii = int(input("Ingrese numero: "))
print(chr(codigoAsccii))"""

""""
#isdigit no valida si es un numero o no
numero = input("Ingrese un numero: ")
if numero.isdigit():
    print("El valor ingresado es numerico")
else:
    print("El valor ingresado NO es numerico")"""

"""#Reemplaza un valor por otro dentro de una cadena
mensaje = input("Ingrese un mensaje: ")
print(mensaje.replace("a", "#"))
print(mensaje.replace(" ", "#"))
lista = mensaje.split(" ")
print(lista)
print(len(lista))
print(len(mensaje))"""

"""valor = input("Ingrese un valor: ")
#reconoce si el valor ingresado es un caracter especial
if valor.isalnum():
    print("Caracter alfanumerico")
else:
    print("Caracter especial")"""

listaPaises = []
listaPaises. append("Peru")
listaPaises.append("Uruguay")
listaPaises.append("Brasil")
print(listaPaises)
listaPaises.remove("Brasil")
print(listaPaises)
listaPaises.insert(1, "VS")
print(listaPaises)
print(listaPaises.count("Peru"))
print(listaPaises.index("Uruguay"))
print(listaPaises.pop())
print(listaPaises)
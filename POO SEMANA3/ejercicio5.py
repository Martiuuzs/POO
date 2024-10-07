"""
Rotar cadena en Python
@author parzibyte
"""
cadena = "Hola"
rotada = ""
rotaciones = 2
for letra in cadena:
    # Sacar su número
    representacion_entera = ord(letra)
    # Concatenar
    rotada += chr(representacion_entera + rotaciones)
print("La cadena {} al ser rotada {} posiciones, se convierte en {}".format(
    cadena, rotaciones, rotada))
# Salida:
# La cadena Hola al ser rotada 2 posiciones, se convierte en Jqnc

#import cuadrado
#import cuadrado as cua (esto le permite cambiar el nombre principal al nombre que queremos)
from cuadrado import ingresarlado, calcarea
from idat.diseñointeriores import primeraSesion
lado1 = ingresarlado()
lado = calcarea(lado1)
print(f"El lado del cuadrado es {lado1}")
print(f"El area del cuadrado es {lado}")
primeraSesion()

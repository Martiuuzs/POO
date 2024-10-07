#importando modulo random
import random, operaciones

#Usando la funcion randint del modulo random
numero1 = random.randint(1,10)
numero2 = random.randint(1,20)
print(f"el primer numero es {numero1}")
print(f"el segundo numero es {numero2}")
print(operaciones.multi(numero1, numero2))
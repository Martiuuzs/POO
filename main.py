from calculadora.operadores import *
num1 = input("Ingrese el primer numero: ")
num2 =  input("Ingrese el segundo numero: ")

print("{} + {} => {}".format(num1,num2, suma(num1, num2)))
print("{} + {} => {}".format(num1,num2, resta(num1, num2)))
print("{} + {} => {}".format(num1,num2, multiplicacion(num1, num2)))
print("{} + {} => {}".format(num1,num2, division(num1, num2)))
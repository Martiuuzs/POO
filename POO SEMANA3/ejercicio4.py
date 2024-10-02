palabra = input("Ingrese una palabra: ")
palabraAlReves = palabra[::-1]
print(palabraAlReves)
if palabra == palabraAlReves:
    print("La palabra es palindromo")
else:
    print("No es palindromo")   
lista_paises =  ["Peru", "Chile", "España", "Argentina", "Ecuador", "Alemania"]
try:
    contador = 0
    while(contador < len(lista_paises)+1):
        print(lista_paises[contador])
        contador += 1
#Un posible error
except IndexError:
    print("Eror, indice fuera de rango")
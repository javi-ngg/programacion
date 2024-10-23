# -------------------------------------Ejercicio 1 --------------------------------
lista = [1, 2, 3, 4, 5]
def funcion(sumar):
    return sumar + 5
lista1 = list(map(funcion, lista))
print(lista1)


# -------------------------------------Ejercicio 2 --------------------------------
lista = ["hola, que, tal", "hola, hola, hola"]
def funcion(titulo):
    return titulo.title()
lista1 = list(map(funcion, lista))
print(lista1)


# -------------------------------------Ejercicio 3 --------------------------------
lista_numeros = [10, 20, 30]
def lista_dupliclar(duplicar):
    return duplicar * 2
lista_final = list(map(lista_dupliclar, lista_numeros))
print(lista_final)


# -------------------------------------Ejercicio 4 --------------------------------
lista_decimales = []
while True:
    ingresar_numeros = float(input("Ingresa numeros decimales hasta poner 0: " ))
    if ingresar_numeros == 0: 
        break
    elif ingresar_numeros != 0:
        lista_decimales.append(ingresar_numeros)

def lista_redondear(ingresar_numeros):
    return round(ingresar_numeros)
lista_final = list(map(lista_redondear, lista_decimales))
print(lista_final)

# -------------------------------------Ejercicio 5 --------------------------------
lista_palabras = []
while True:
    ingresar_palabras = str(input("Dame palabras hasta poner fin: ")).lower()
    if ingresar_palabras == "fin":
        break
    elif ingresar_palabras != "fin":
        lista_palabras.append(ingresar_palabras)

def lista_longitud(ingresar_palabras):
    return len(ingresar_palabras)
lista_final = list(map(lista_longitud, lista_palabras))
print(lista_final)

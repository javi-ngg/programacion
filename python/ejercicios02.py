# EJERICICO 1

palabra = input("Introduce una palabra: ")
palabra_invertida = ""
for letra in palabra:
    palabra_invertida = letra + palabra_invertida
print("La palabra invertida es:", palabra_invertida)

# EJERCICIO 2
suma_total = 0
conteo = 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    
    if numero == 0:
        break
    suma_total += numero
    conteo += 1
if conteo > 0:
    promedio = suma_total / conteo
    print(f"El promedio de los números introducidos es {promedio}.")
else:
    print("No se introdujeron números.")

# EJERCICIO 3

nombres = []
while True:
    nombre = input("Introduce un nombre (escribe 'fin' para terminar): ")
    
    if nombre.lower() == "fin": 
        break
    nombres.append(nombre)
print(f"Los nombres ingresados son: {nombres}")
print("\nLista de nombres:")
for nombre in nombres:
    print(f"- {nombre}")

# EJERCICIO 4

contraseña_correcta = "python123"
while True:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == contraseña_correcta:
        print("¡Acceso concedido!")
        break 
    else:
        print("Contraseña incorrecta, intenta de nuevo.")


# EJERCICIO 5

numeros = []
while True:
    entrada = input("Introduce un número (escribe 'hecho' para terminar): ")
    
    if entrada.lower() == "hecho":
        break
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un número válido o 'hecho' para terminar.")
if numeros:
    numero_mayor = max(numeros) 
    print(f"El número mayor ingresado es {numero_mayor}.")
else:
    print("No se ingresaron números.")
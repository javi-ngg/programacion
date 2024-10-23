#EJERCICIO 1

num1 = float(input("Dime el primer numero"))
num2 = float(input("Dime el segundo numero"))

operacion = str(input("Que operación quieres hacer"))

if operacion == "suma":
    resultadosuma = num1 + num2
    print("La suma es:", resultadosuma)
elif operacion == "resta":
    resultadoresta = num1 - num2
    print("La resta es", resultadoresta)
elif operacion == "multiplicacion":
    resultadomultiplicacion = num1 * num2
    print("La multiplicación es", resultadomultiplicacion)
elif operacion == "division":
    resultadodivision = num1 / num2
    print("La division es", resultadodivision)
else:
    print("no valido")


#EJERCICIO 2

num1 = float(input("Dime un numero par o impar: "))

if num1 % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


#EJERCICIO 3

num = int(input("Dime un numero: "))
suma = 0
for jorgefloyd in range(1, num+1):
    suma += jorgefloyd
print("El resultado es: ", suma)


#EJERCICIO 4








#EJERCICIO 5

num = 16
maeb = int(input("Adivina el numero:"))

while maeb != num:
    if maeb < num:
        print("No, mas alto")
    elif maeb > num:
        print("No, mas bajo")
    maeb = int(input("Adivina el numero:"))

print("Lo has adivinado payaso")


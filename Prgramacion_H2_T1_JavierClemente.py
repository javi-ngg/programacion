#---------------------------------------------------Ejercicio 1--------------------------------------------------------------------

# Este def hace que en un rango desde 0 hasta llegar al número de lados mutliplique el "*" 
# por el numero de lados, entonces se mostrara tantos asteriscos como lados haya.
def mostrar_cuadrado(lado):
    for i in range(lado):
        print('*' * lado)

# Hacemos la correspondiente operación para calcular el área y el perímetro.        
    area = lado * lado
    perimetro = 4 * lado
    print(f"Su área es {area}")
    print(f"Su perímetro es {perimetro}")

# Hacemos elle def exactamente igual para el rectángulo.
def mostrar_rectangulo(base, altura):
    for i in range(altura):
        print('*' * base)

# Calculamos el área y perímetro del rectángulo.
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Su área es {area}")
    print(f"Su perímetro es {perimetro}")

#Este def con un bucle dentro simplemente para crear el menu donde se preguntará al usuario que opción quiere elegir.
def menu():
    while True:
        print("1- Cuadrado")
        print("2- Rectángulo")
        print("3- Salir")
        opcion = input("Dime una opción: ")
    
    # Creamos la primera opción para preguntar y después mostrar el cuadrado.
        if opcion == '1':
            lado = int(input("Dime el lado del cuadrado: "))
            mostrar_cuadrado(lado)
            

# Creamos una segunda opción para preguntr y después mostrar el rectángulo.      
        elif opcion == '2':
            base = int(input("Dime la base del rectángulo: "))
            altura = int(input("Dime la altura del rectángulo: "))
            mostrar_rectangulo(base, altura)

#Y este tercer elif para el 0.5 extra para que me pregunta salir.
        elif opcion == '3':
            print("Has salido del programa")
            break
        else:
            print("Opción incorrecta")
            
menu()



#---------------------------------------------------Ejercicio 2--------------------------------------------------------------------

#Lo primero que hago es darle un valor a "piedra", "papel", y "tijeras" el valor puede ser el que quiera
piedra = 1 
papel = 2
tijeras = 3

#Esto es para el 0.5 puntos extras que es un contador que esta en cero, que es el contador de victoria del bot y del mio
contador_bot = 0
contador_persona = 0

#Aquí ponemos el nombre a una variabla y hacemos que sea random y le damos un rango de numeros.
import random
aleatorio = random.randint(1, 3)


#Empezamos el bucle y para que decirle que se siga ejecutando hasta que el contador llegue a 3.
#Lo que ponemos es "contarador_bot != 3" lo que hace != es que mientras sea diferente de 3 el contador de bot se siga.
while contador_bot != 3 and contador_persona != 3:
    persona = int(input("Elige: 1-Piedra, 2-Papel, 3-Tijeras: ")) 

#Empezamos con los if, y lo que le decimos que tiene que hacer en este if es que cuando la persona y la maquina eligan 1,
#que uno es piedra le diga que han quedado empate.
    if persona == 1 and aleatorio == 1:
        print("El bot ha elegido piedra y tu también, habéis quedado empate")
        aleatorio = random.randint(1, 3)

#Este es diferente al anterior ya que en este caso no es empate y le tengo que especificar que el bot ha ganado y que tiene
#que sumar 1 al contador. Y hacer un "print" de el contador del que acaba de ganar esa jugada.
    elif persona == 1 and aleatorio == 2:
        print("El bot ha elegido papel y tu piedra el bot ha ganado")
        contador_bot = contador_bot +1
        print(f"El bot lleva {contador_bot} partidas ganadas.")
        aleatorio = random.randint(1, 3)

    elif persona == 1 and aleatorio == 3:
        print("El bot ha elegido tijeras y tu piedra has ganado")
        contador_persona = contador_persona +1
        print(f"Tu llevas {contador_persona} partidas ganadas.")
        aleatorio = random.randint(1, 3)

    elif persona == 2 and aleatorio == 2:
        print("El bot ha elegido papel y tu también, habéis quedado empate")
        aleatorio = random.randint(1, 3)

    elif persona == 2 and aleatorio == 1:                          #Todos los demas if van igual que los 2 que he documentado.
        print("El bot ha elegido piedra y tu papel has ganado")
        contador_persona = contador_persona + 1
        print(f"Tu llevas {contador_persona} partidas ganadas.")                    
        aleatorio = random.randint(1, 3)

    elif persona == 2 and aleatorio == 3:
        print("El bot a sacado tijeras y tu papel el bot ha ganado")
        contador_bot = contador_bot +1
        print(f"El bot lleva {contador_bot} partidas ganadas.")
        aleatorio = random.randint(1, 3)

    elif persona == 3 and aleatorio == 3:
        print("El bot ha elegido tijeras y tu también, habéis quedado empate")
        aleatorio = random.randint(1, 3)

    elif persona == 3 and aleatorio == 1:
        print("El bot ha sacado piedra y tu tijeras has perdido")
        contador_bot = contador_bot +1
        print(f"El bot lleva {contador_bot} partidas ganadas.")
        aleatorio = random.randint(1, 3)

    elif persona == 3 and aleatorio == 2:
        contador_persona = contador_persona +1
        print(f"El bot lleva {contador_persona} partidas ganadas.")
        aleatorio = random.randint(1, 3)

#Por si se escribe algo no valido.
    else:
        print("Escribe algo valido")
        break

#Y una vez el contador de bot o de persona llega a 3 se hace un print del resultado diciendo quien a ganado
if contador_bot == 3:
    print("El bot ha llegado a las 3 partidas ganadas, ha ganado.")

elif contador_persona == 3:
    print("Has llegado a las 3 partidas ganadas, has ganado.")




#---------------------------------------------------Ejercicio 3--------------------------------------------------------------------
#Aquí empiezo con un bucle en el cual con la variable "saldo_inicial" le digo que me diga un saldo inicial.
while True:               
    saldo_inicial = float(input("Dime el saldo inicial de tu cuenta: "))   

#Y con el if le digo que en el caso que el saldo sea menor que 0 me pida que escriba un número mayor que 0 
    if saldo_inicial < 0:   
        print("Escribe un numero mayor que 0: ")

    elif saldo_inicial >= 0:
        break

#Estas variables son para los 0,5 puntos extra. Lo que es un contador para las veces que he ingresado y retirado.
ingresos = 0
retiradas = 0

#Empiezo un bucle en el cual le pido con un variable que eliga entre diferentes opciones del uno a 5,
#para que solo me pueda dar numeros pongo "int".
while True:
    elegir = int(input("1-Ingresar dinero, 2-Retirar dinero, 3-Mostrar saldo, 4-Salir, 5-Estadisticas: "))
        
#El siguiente if y elif son practicamente iguales, le digo que elijo el numero 1 que es ingresar dinero
#Le pido cuanto dinero quiere ingresar y le especifico que sume a saldo inicial el numero que le acabo de dar
#(Lo mismo para el primer elif pero restando")
    if elegir == 1:
        ingresar = float(input("Cuanto dinero quieres ingresar: "))
        saldo_inicial = saldo_inicial + ingresar
        ingresos = ingresos + 1

    elif elegir == 2:
        retirar = float(input("Cuanto dinero quieres retirar: "))
        saldo_inicial = saldo_inicial - retirar
        retiradas = retiradas + 1

#Con este elif le digo que me muestre el saldo inicial que es el saldo actual que tenga
    elif elegir == 3:
        print(f"Este es tu saldo actual: {saldo_inicial}")

#Con este elif sales del programa con break
    elif elegir == 4: 
        print("Has salido de mi programa ")
        break

#Al elegir esta opción me muestra las veces que he ingresado o retirado dinero. (El 0.5 extra)
    elif elegir == 5:
        print(f"Las retiradas totales han sido: {retiradas}, y los ingresos totales han sido: {ingresos}")

#Y por último este else es por si se escribe algún número que no sea del 1 al 5 que te vuelva a pedir un número
#del 1 al 5
    else:
        print("Elige una opción correcta.")
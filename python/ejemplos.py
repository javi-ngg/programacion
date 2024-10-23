edad = int(input("Dime cual es tu edad:"))

if edad < 5:
    print("La entrada es gratuita")
elif edad >= 5 and edad <= 12:
    print("la entrada cuesta 5 euros")
elif edad >= 13 and edad <= 17:
    print("la entrada cuesta 7 euros")
else:
    print("la entrada cuesta 10 euros")


nota = int(input("Dime cual a sido tu nota:"))

match nota:
        case 90:
            print("A")
        case 80:
            print("B")
        case 70:
            print("C")
        case 60:
            print("D")
        case _:
            print("F")


numero = int(input("Dime un numero correpondiente a un dia de la semana: "))

match numero:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        case _:
            print("No valido")


idioma = input("Escribe en que idioma quieres ver un mensaje: ")

match idioma:
    case "español":
        print("Esto es un mensaje en tu idioma")

    case "ingles":
        print("This is a message in your idiom")

    case "frances":
        print("Ceci est un message dans votre langue")

    case _:
        print("Idioma no soportado")















edad = 15
es_estudiante = True

if edad < 18 and es_estudiante:
    print("Eres mayor de edad")
elif edad < 18 and not es_estudiante:
    print("Es menor de edad pero no es estudiante")
else:
    print("Es mayor de edad")



a = 10
b = 10

if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual que b")

    
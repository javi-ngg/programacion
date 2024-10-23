def menu():
    print("*** Ejecución Iniciada. ***")
    print("MENU")
    print("1 - Cuadrado")
    print("2 - Rectángulo")

def calculate_square():
    side = float(input("Dime el lado del cuadrado: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"Su área es {area}")
    print(f"Su perímetro es {perimeter}")

def calculate_rectangle():
    base = float(input("Dime la base del rectángulo: "))
    height = float(input("Dime la altura del rectángulo: "))
    area = base * height
    perimeter = 2 * (base + height)
    print(f"Su área es {area}")
    print(f"Su perímetro es {perimeter}")

def main():
    while True:
        menu()
        option = input("Dime una opción: ")
        if option == '1':
            calculate_square()
            break
        elif option == '2':
            calculate_rectangle()
            break
        else:
            print("Opción incorrecta")
        
main()
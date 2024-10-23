lista1 = [1,2,3,4]

tupla1 = (1,2,3,4)

print("Valor de la lista")
print(lista1)

print("Valor de la tupla")
print(tupla1)

lista1[0] = 10
print("Valor de la lista")
print(lista1)

lista1[0] = 10
print("Valor de la tupla")
print(tupla1)

dic1 = {}

nombre = input("introduce el nombre del nuevo contacto: ")
telefono = input(f"introduce el teléfno de {nombre}")

dic1[nombre] = telefono

print("Esta es tu agenda")
print(dic1)

print("Vamos a modificar el teléfono de un contacto: ")
nombre_busqueda = input("Dame el nombre del contacto que quieres cambiar: ")
telefono_nuevo = input("dame el nueo número de teléfono: ")

dic1[nombre_busqueda] = telefono_nuevo

print(dic1)


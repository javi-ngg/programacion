lista_reproduccion = []

cancion = input("Dame el nombre de una canción: ")

while cancion != "fin":
    lista_reproduccion.append(cancion)
    cancion = input("Dame el nombre de una canción:  ").lower()


while True:
    cancion = input("Dame el nombre de una canción:  ").lower()
    if cancion != "fin":
        lista_reproduccion.append(cancion)
    else:
        break
print(lista_reproduccion)

for i in len(lista_reproduccion):
    print(f"{i}.- {lista_reproduccion[i]}")

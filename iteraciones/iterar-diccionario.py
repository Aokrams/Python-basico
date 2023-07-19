# para iterar sobre un diccionario se hace con las llaves
# llave toma el valor de las llaves osea nombre y color, despues le dijo que imprima la llave de frutas
frutas = {
    "nombre": "manzana",
    "color": "roja"
}

for llave in frutas:
    print(llave, frutas[llave])


# se puede imprimir solo las llaves usando .keys()
for elemento in frutas.keys():
    print(elemento)


# se puede imprimir solo el valor de las llaves usando .values()
for elemento in frutas.values():
    print(elemento)


# tambien se pueden imprimir las llaves y valores juntas usando .items() asignando 2 valores en el for
for llave, valor in frutas.items():
    print(llave, valor)


# y se puede usar .items() con un solo valor en el for para imprimir llave y valor como una tupla
for elemento in frutas.items():
    print(elemento)
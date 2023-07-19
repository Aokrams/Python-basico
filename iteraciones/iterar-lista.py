# para iterar sobre una lista se puede ocupar for o while dependiendo de que prefiera el desarrollador
# para iterar con for sobre el nombre 
animales = ["Perro", "Gato", "Conejo"]
for animal in animales:
    print(animal)


# para iterar sobre el indice usando for, se combina range con len, range para que imprima 
# todos los numeros de acuerdo a cuantos elementos tenga la lista, en este caso 3
# asi que range imprimira desde 0 hasta 2 que vendrian a ser los index
for index in range(len(animales)):
    print("indice", index, "elemento", animales[index])


# para iterar con while usanmos len para saber cuanto mide la lista
# y luego sumamos la variable para que pase al siguiente
mide = 0

while mide < len(animales):
    print(animales[mide])
    mide += 1
# las listas se pueden hacer de cualquier cosa
# se imprimen en el orden en el que son definidas
lenguajes = ["Python", "Java", "JavaScript"]
print(lenguajes)

# no necesariamente deben tener un solo tipo de dato
lista = [1, 1.9, True, "jeje", 1]
print(lista)

# para obtener el elemento con el indice 2 se escribe entre []
print(lenguajes[2])

# para saber cuantos elementos hay en la lista se escribe len() 
print(len(lenguajes))

# para obtener el ultimo elemento de una lista se llaman con [-1] asignando el -1 como el ultimo
print(lenguajes[-1])

# se asigna el ultimo elemento como -1, el penultimo como -2, el antepenultimo -3 y asi sucesivamente
print(lenguajes[-2])
print(lenguajes[-3])

# se puede llamar x cantidad de elementos de la lista utilizando 
# [desde que indice : cuantos elementos quieres llamar]
print(lenguajes[0:2])

# tambien podemos meter una lista dentro de otra
programador = [lenguajes, "Versado", "Guapo"]
print(programador)

# si queremos llamar "Java", que esta dentro de lenguajes, desde la lista programador utilizamos
# [posicion de lenguajes][posicion de "Java"] 
print(programador[0][1])

# para reemplazar un valor dentro de una lista 
lenguajes[2] = "golang"
print(lenguajes)

# para añadir elementos a la lista utilizamos .append(), esta agregara elementos al final de la lista
lenguajes.append("JavaScript")
print(lenguajes)

# para unir 2 listas se usa .extend()
otrosLenguajes = ["c", "c++"]
lenguajes.extend(otrosLenguajes)
print(lenguajes)
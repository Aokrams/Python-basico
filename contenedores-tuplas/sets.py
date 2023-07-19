# los sets son una estructura desordenada no se pueden llamar mediante el indice y se definen
# set={}
set1 = {1, 2, 3}
print(set1)

# solo contienen elementos unicos y si intentamos repetirlos no funcionara
set2 = {1, 1, 1, 2, 3}
print(set2)

# pueden contener elementos de diferentes tipos pero estos son inmutables 
set3 = {1, 9.1, "texto"}
print(set3)

# para agregar elementos a un set se utiliza .add()
set1.add(4)
print(set1)

# para agregar varios elementos a un set utilizamos .update([])
set1.update([4, 5, 6])
print(set1)

# para saber cuantos elementos tiene el set utilizamos len()
print(len(set1))

# para eliminar elementos del set utilizamos .discard()
set1.discard(1)
print(set1)

# tambien se puede utilizar .remove() para eliminar un elemento, pero dara error 
# si el elemento ya fue eliminado con anterioridad
set1.remove(2)
print(set1)

# para eliminar todos los elementos de un set utilizamos .clear()
set1.clear()
print(set1)
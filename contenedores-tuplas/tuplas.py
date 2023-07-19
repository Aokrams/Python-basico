# las tuplas son parecidas a las listas pero con la diferencia de que son inmutables 
# (no se pueden modificar) y se definen entre () o simplemente por comas
animales = ("Perro", "Gato", "Conejo")
print(animales)
animales = "Perro", "Gato", "Conejo"
print(animales)

# para llamar a los elementos mediante el indice, se hace igual que las listas []
print(animales[1])

# para llamar al ultimo elemento
print(animales[-1])

# si queremos cambiar el valor de algun elemento, nos dara ERROR
animales[2] = "buey"
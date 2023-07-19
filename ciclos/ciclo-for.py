# los for sirven para iterar sobre cada letra en un string o sobre cada elemento en una lista
# aqui itera sobre un string
for letra in "Hola":
    print(letra) 


# aqui itera sobre una lista
dulces = ["Caramelo", "Galleta", "Helado"]
for dulce in dulces:
    print(dulce)


# break se utiliza para romper el ciclo
# en este caso se romperia despues de hacer el ciclo una vez
dulces = ["Caramelo", "Galleta", "Helado"]
for dulce in dulces:
    print(dulce)
    break


# break se usa generalmente dentro de un if
# aqui se rompe cuando llegue a galleta
dulces = ["Caramelo", "Galleta", "Helado"]
for dulce in dulces:
    print(dulce)
    if dulce == "Galleta":
        break


# continue se usa para saltar las lineas de codigo que esten despues de continue
# en este caso se salta el print cuando este en caramelo y hace el ciclo denuevo
dulces = ["Caramelo", "Galleta", "Helado"]
for dulce in dulces:
    if dulce == "Caramelo":
        continue 
    print(dulce)


# range() crea una lista de numeros desde el 0 hasta el numero anterior que pongamos adentro
# en este caso empieza del 0 y se detiene en el 9
for numeros in range(10):
    print(numeros)


# range() tambien puede tener 2 numeros dentro, el primero que indique desde que numero empezar
# y el segundo que indica hasta que numero detenerse
# en este caso se detine en el 10 y empieza en el 1
for numeros in range(1, 11):
    print(numeros)
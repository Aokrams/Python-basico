# las condiciones nos permiten realizar una accion si estas se cumplen o realizar otra si no lo hacen
# se escriben, if condicion: accion a relizar si se cumple  else: accion a realizar si no se cumple
a = 1
b = 1

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")


# no solo sirven para comparar
c = False

if c:
    print("C es verdadero")
else:
    print("C es falso")


# se puede usar is en ocasiones, para comparar
d = True

if type(d) is bool:
    print("D es booleano")
else:
    print("D es otro tipo de dato")


# se ocupa and para que se cumplan varias condiciones
e = 10
f = 5
g = 1

if e > f and f > g:
    print("Las 2 condiciones son verdaderas")


# se ocupa or para validar si al menos una de las condicones se cumple
h = 9
i = 1
j = 4

if h > j or j == i:
    print("Una de las condicones se cumplio")
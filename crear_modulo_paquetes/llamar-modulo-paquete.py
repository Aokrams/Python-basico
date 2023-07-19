# aqui llamaremos las funciones de nuestro modulo importandolo
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado

# llamaremos la funcion dentro de una tupla
lado = 10

cuadrado = {
    "Lado": lado,
    "Area": area_cuadrado(lado),
    "Perimetro": perimetro_cuadrado(lado)
}

# aqui lo llamaremos y la funcion hara todo el trabajo de calculo dentro de la tupla
print(cuadrado)

# tambien podemos llamar la funcion normalmente en una variable
area = area_cuadrado(4)
print(area)


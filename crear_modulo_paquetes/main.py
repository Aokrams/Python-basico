# aqui llamaremos a las funciones dentro del paquete
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 5

cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print("Cuadrado:", cuadrado)

radio = 6

circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print("Cirdulo:", circulo)
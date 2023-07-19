# las funciones con parametros son las que llevan una variable indefinida dentro de los ()
# se usa la f en el print() para que tome lo que este dentro de {} como un valor y no como string
def calcular_area(ancho, largo):
    area = ancho * largo
    print(f"El area es de {area}")

# se puede llamar de 2 formas 
calcular_area(9, 14)
calcular_area(ancho= 9, largo= 14)
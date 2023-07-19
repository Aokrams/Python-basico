# las funciones con retorno se hacen si quiero ocupar el valor que me de una funcion 
# para usarlo como una variable en otro lugar
def area_cuadrado(ancho):
    area = ancho * ancho
    return area

def perimetro_cuadrado(ancho):
    perimetro = ancho * 4
    return perimetro

area = area_cuadrado(10)
perimetro = perimetro_cuadrado(10)

print(f"Area del cuadrado: {area}, Perimetro del cuadrado: {perimetro}")

# tambien podemos hacer que una funcion devuelva varios valores
def calcular_rectangulo(ancho, largo):
    area_rec = ancho * largo
    perimetro_rec = ancho * 2 + largo * 2
    return area_rec, perimetro_rec

area_rec, perimetro_rec = calcular_rectangulo(5, 10)

print(f"El area del rectangulo es: {area_rec}, El perimetro del rectangulo es: {perimetro_rec}")

# se pueden guardar en una tupla las 2 variables de la funcion si solo queremos definirla 
# en una variable

resultado = calcular_rectangulo(3, 8)
print(resultado)
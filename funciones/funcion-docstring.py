# la documentacion de una funcion es un comentario hecho por el que creo la funcion, con el fin
# de hacer entender para que sirve la funcion o que errores puede llegar a tener
def perimetro_cuadrado(lado):
    """esta funcion permite calcular el perimetro de un cuadrado
    
    esta funcion recibe como parametro el valor de un lado del 
    cuadrado y calcular ese valor por 4 al ser un cuadrado

    Args:
        lado (int): medida del lado del cuadrado

    Returns:
        perimetro (int): primetro del cuadrado
    """
    perimetro = lado * 4
    return perimetro

# cuando se llame a la funcion, al pasar el mouse por encima dara la descripcion que le dimos 
# anteriormente en base a la primera linea como titulo y el resto mas detallado
perimetro_cuadrado(5)
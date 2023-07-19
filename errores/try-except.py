# try except permite capturar errores y manejarlos, try son instrucciones que se ejecutan 
# y except son instrucciones que se ejecutan si algo del bloque try falla
def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio(lista = ["perro"])
    print(promedio)
# solo toma los assertionerror cuando este esta dentro de la funcion
except AssertionError as assert_error: 
    print(assert_error)
# tambien permite capturar el error para ver por que fallo usando Exception as any
except Exception as error:
    print("La funcion no calculo el promedio")
    print(error)
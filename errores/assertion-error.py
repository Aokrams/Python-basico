# los assert error son errores que se levantan al cumplir la condicion son diferentes de los 
# exception porque no es necesario escribir explicitamente la condicion
def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[])
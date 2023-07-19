# los errores de excepcion son errores que aunque este bien escrito de error
# si queremos que una funcion nos de error utilizamos raise exception  
def validar_x(x):
    if x < 1:
        raise Exception("X debe ser mayor a 1")
    else:
        print("X es mayor a 1")

x = 2
validar_x(x)
# para crear una funcion se escribe def para comenzarla
# hay variables locales(se definen y usan solo dentro de la funcion) y hay varibles 
# globales(se definen fuera de la funcion generalmente al principio y en mayuscula, 
# se usan dentro y fuera de la funcion)
APELLIDO = "Lopez"

def funcion():
    nombre = "Brandon"
    print("Mi primera funcion en Python")
    print(nombre, APELLIDO)

# para invocarla solo se escribe la funcion sin el def
funcion()
print(APELLIDO)
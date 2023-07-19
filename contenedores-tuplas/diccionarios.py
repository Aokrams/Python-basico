# los diccionarios son conocidos en otros lenguajes como el json, utilizan una definicion, una 
# llave y un valor, definicion = {"llave": valor}
# las llaves son de tipo texto y los valores pueden ser de cualquier tipo
fruta = {
    "nombre": "manzana",
    "peso": 100
}
print(fruta)

# para obtener un valor de utiliza la llave, definicion["llave"]
print(fruta["nombre"])

# para añadir un elemento al diccionario 
fruta["color"] = "rojo"
print(fruta)

# los diccionarios no pueden tener llaves repetidas y si lo intentamos solo sobreescribiremos 
# la llave anterior
fruta["color"] = 2
print(fruta)

# los valores pueden ser de cualquier tipo
fruta["acciones"] = ["rueda", "cae", "posa"]
print(fruta)

# los diccionarios tienen funciones como
# .items() que devuelve una lista de tuplas con la llave y el valor
print(fruta.items())

# .keys() que devuelve una lista de las llaves del diccionario
print(fruta.keys())

# .values() que devuelve una lista de los valores del diccionario
print(fruta.values())
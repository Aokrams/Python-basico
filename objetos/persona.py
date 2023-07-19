# para definir una clase usamos class y la primera letra en mayuscula
# para crear el constructor de una clase usamos el def __init__(self): como parametro de la funcion
# init crea el constructor de la clase
# los atributos son valores que se le dan a la clase y pueden ser definidos dentro de los parametros
# o asignandole un valor a la clase
class Persona:
    atributo = 123
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # para definir los metodos de una clase se usa self como primer parametro
    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")
        
brandon = Persona("brandon", 22)
print(brandon.nombre)
print(brandon.edad)
print(brandon.atributo)

# para llamar el metodo se usa, objeto.metodo()
brandon.cumplir_anios()

# esto nos retorna falso ya que al ser ambos del mismo tipo, no son el mismo objeto
dorado = Persona("dorado", 3)
print(brandon == dorado)


# para usar la herencia para una clase hija que salga de la clase padre Persona
# las clases hijas heredan todos los atributos y metodos e la clase padre, ademas
# de incluir todos los metodos de la clase hija
# para agregar nuevos atributos a la clase hija, se define el constructor y se colocan todos los 
# atributos nuevos y los de la clase padre, como parametros, luego se utiliza super() colocando
# el nombre de la clase hija(esta) y self, luego un .__init__() con los parametros de 
# la clase padre, despues se define cada atributo de la clase hija
class Gamer(Persona):
    def __init__(self, horas_totales, nombre, edad):
        super(Gamer, self).__init__(nombre, edad)
        self.horas_totales = horas_totales
    def jugar(self, horas_jugadas):
        self.horas_totales += horas_jugadas
        print(f"Usted ha jugado {horas_jugadas} horas")
        print(f"Horas totales jugadas: {self.horas_totales}")

jorge = Gamer(20, "Jorge", 20)
jorge.jugar(3)
jorge.cumplir_anios()
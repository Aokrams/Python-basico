# para importar un modulo o paquete usamos import y su nombre
import datetime

# la llamamos asi
hora_actual = datetime.datetime.now()
print(hora_actual)

# tambien podemos darle un nombre a la importacion para que sea mas corta usando as
import datetime as dt

h_actual = dt.datetime.now()
print(h_actual)

# tambien podemos importar solo el submodulo que esta dentro de otro modulo
# por ejemplo el submodulo datetime que esta dentro del modulo datetime usando from
from datetime import datetime

hor_actual = datetime.now()
print(hor_actual)
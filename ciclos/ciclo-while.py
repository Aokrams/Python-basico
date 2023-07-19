# while se ocupa con una condicion 
# en este caso si a es menor o igual a 10 se imprimira a en la terminal
# generalmente se ocupa break para detener el ciclo ya que puede llegar a ser infinito
a = 1

while a <= 10:
    print(a)
    a += 1
    if a == 7:
        break
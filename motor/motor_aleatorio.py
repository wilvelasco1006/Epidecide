# Implementación del motor aleatorio, un generador de números pseudoaleatorios.
# Para evitar el uso de libreria random. Usamos un generador congruencial lineal (LCG).

class MotorAleatorio:
    def __init__(self, semilla):
        self.semilla = semilla  # Semilla inicial para el generador
        self.estado = semilla

    # Funcion que genera un número pseudoaleatorio flotante entre 0 y 1.
    def aleatorio(self):
        # Parámetros del generador congruencial lineal (LCG)
        a = 1664525 # Multiplicador
        c = 1013904223 # Incremento
        m = 2**32  # Modulo para mantener el rango de 0 a 1

        # Actualiza el estado usando la fórmula LCG
        self.estado = (a * self.estado + c) % m
        return self.estado / m  # Devuelve un número entre 0 y 1
    
    # Funcion que retorna un entero entre minimo y máximo (incluidos).
    def entero(self, minimo, maximo):
        fraccion = self.aleatorio() # Genera un número aleatorio entre 0 y 1
        rango = maximo - minimo + 1 # Calcula el rango de valores posibles
        return minimo + int(fraccion * rango)   # Convierte la fracción a un entero en el rango deseado

    # Funcion que retorna un elemento aleatorio de una lista.
    def elegir(self, lista):

        if len(lista) == 0:
            return None  # Si la lista está vacía, retorna None
        indice = self.entero(0, len(lista) - 1) # Genera un índice aleatorio entre 0 y el tamaño de la lista - 1
        return lista[indice] # Retorna el elemento en el índice aleatorio de la lista
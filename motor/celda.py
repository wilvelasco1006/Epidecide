from modelos.estado_celda import EstadoCelda # Importamos la clase EstadoCelda

"""
Representa una celda del autómata celular (un individuo).
Contiene su estado actual y un estado futuro provisional para actualizar en sincronía.
"""
class Celda:

    # Inicializa una celda con un estado inicial.
    def __init__(self, estado_inicial):
        self.estado = estado_inicial # Estado actual de la celda
        self.proximo_estado = estado_inicial # Estado temporal para la siguiente iteración

    # funcion que define el estado que tomara la siguiente iteración
    def definir_proximo_estado(self, nuevo_estado):
        self.proximo_estado = nuevo_estado # Actualiza el estado provisional

    # Actualiza el estado actual al provisional.
    def actualizar_estado(self):
        self.estado = self.proximo_estado # Cambia el estado actual al provisional

    # Funcion que retorna si esta infectado
    def esta_infectado(self):
        return self.estado == EstadoCelda.INFECTADO

    # Funcion que retorna si esta susceptible
    def esta_susceptible(self):
        return self.estado == EstadoCelda.SUSCEPTIBLE
    # Funcion que retorna si esta recuperado
    def esta_recuperado(self):
        return self.estado == EstadoCelda.RECUPERADO
    
    # Funcion que retorna si esta fallecido
    def esta_fallecido(self):
        return self.estado == EstadoCelda.FALLECIDO
    
    # Funcion que devuelve el simbolo  para mostrar por consola
    def simbolo(self):
        return EstadoCelda.a_texto(self.estado)  # Usa el método estático para obtener el símbolo del estado actual

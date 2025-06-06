from modelos.estado_celda import EstadoCelda  # Importamos la clase EstadoCelda

"""
    Clase que recolecta estadísticas de la simulación paso a paso.
    Guarda la evolución de los estados (S, I, R, F) y calcula indicadores finales.
"""
class RecolectorEstadisticas:
    def __init__(self):
        self.historial = []  # Lista para almacenar el historial de estados en cada paso

    # Funcion que almacena los valores de S I R F para un paso dado.
    def registrar(self,paso,conteo_por_estado):
        entrada = {
            "paso": paso,  # Guarda el número de paso
            "S": conteo_por_estado.get(EstadoCelda.SUSCEPTIBLE, 0),  # Susceptibles
            "I": conteo_por_estado.get(EstadoCelda.INFECTADO, 0),  # Infectados
            "R": conteo_por_estado.get(EstadoCelda.RECUPERADO, 0),  # Recuperados
            "F": conteo_por_estado.get(EstadoCelda.FALLECIDO, 0)  # Fallecidos
        }
        self.historial.append(entrada) # Agrega la entrada al historial

    # Funcion que devuelve el historial de estados.
    def obtener_historial(self):
        return self.historial # Devuelve la lista completa de paso registrados
    
    """
    Funcion que calcula el
    pico de infectados
    paso en que ocurre el pico de infectados
    ataque final (proporción de infectados al final)
    duración de la epidemia (Hasta que I = 0)
    """
    def calcular_metricas_finales(self):
        # Inicializa las variables para calcular las métricas finales
        pico = 0
        paso_pico = 0
        total_infectados = 0
        duracion = 0

        for entrada in self.historial: # Recorre cada entrada del historial
            i = entrada["I"] # si "i" es el número de infectados en el paso actual
            if i > pico: # Si el número de infectados en este paso es mayor que el pico registrado
                pico = i # entonces actualiza el pico
                paso_pico = entrada["paso"] # y guarda el paso en que ocurrió el pico
            total_infectados += i # Suma el número de infectados al total acumulado
            if i > 0: # si hay infectados en este paso
                duracion = entrada["paso"] # entonces actualiza la duración de la epidemia al paso actual
        

        
        # Devuelve un diccionario con las métricas finales
        return {
            "pico_infectados": pico,
            "paso_pico": paso_pico,
            "duracion": duracion,
            "total_infectados_acumulado": total_infectados,

        }
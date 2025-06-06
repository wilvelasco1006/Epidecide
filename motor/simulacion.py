from motor.grilla import Grilla # Importa la clase Grilla desde el módulo grilla
from estadisticas.recolector import RecolectorEstadisticas # Importa la clase RecolectorEstadisticas desde el módulo recolector

"""
Clase principal que coordina la simulación del autómata celular.
grilla, pasos, estadisticas, visualizacion

"""
class Simulacion:

    def __init__(self, tamano, beta, gamma, mu, pasos_totales, motor_aleatorio):
        self.pasos_totales = pasos_totales  # Número total de pasos a simular
        self.grilla = Grilla(tamano, beta, gamma, mu, motor_aleatorio)
        self.grilla.infectar_central()
        self.recolector = RecolectorEstadisticas()  # Inicializa el recolector de estadísticas

    # Funcion que ejcuta la simuación por el numero total de pasos
    # Si mostrar es True, imprime la grilla en cada paso.
    def ejecutar(self, mostrar=False):
        for paso in range(self.pasos_totales): # Repite el proceso por el número de pasos especificado
            conteo = self.grilla.contar_por_estado() # Cuenta los estados actuales de la grilla
            self.recolector.registrar(paso, conteo)  # Registra el conteo en el recolector de estadísticas
            if mostrar:
                print("Paso", paso)
                self.grilla.mostrar_consola()  # Muestra la grilla en la consola
            self.grilla.aplicar_reglas() # Aplica las reglas de transición a todas las celdas
            self.grilla.actualizar_estados() # Actualiza los estados de las celdas al siguiente estado provisional

            # Funcion que devuelve el resumen de la simulación(metricas finales)
    def obtener_estadisticas(self):
        # Devuelve las métricas finales calculadas por el recolector de estadísticas
        return self.recolector.calcular_metricas_finales()


    # Funcion que devuelve la lista de resultados por paso (historial)
    def obtener_historial(self):
        return self.recolector.obtener_historial()

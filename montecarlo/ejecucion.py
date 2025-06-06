from motor.simulacion import Simulacion  # Importa la clase Simulacion desde el módulo motor
from motor.motor_aleatorio import MotorAleatorio  # Importa la clase MotorAleatorio desde el módulo motor_aleatorio

"""
Esta clase Ejecuta múltiples simulaciones independientes con diferentes semillas,
y calcula estadísticas promedio.
"""
class EjecutorMonteCarlo:

    def __init__(self, repeticiones, tamano, beta, gamma, mu, pasos_totales):
        self.repeticiones = repeticiones
        self.tamano = tamano
        self.beta = beta
        self.gamma = gamma
        self.mu = mu
        self.pasos_totales = pasos_totales
        self.resultados = []  # Lista para almacenar los resultados de cada simulación

    # Funcion que ejecuta todas las simulaciones con distintas semillas
    def ejecutar_todas(self):
        for i in range(self.repeticiones):
            semilla = 1000 + i # Genera una semilla única para cada repetición
            motor = MotorAleatorio(semilla)  # Crea un motor aleatorio con la semilla
            sim = Simulacion(self.tamano, self.beta, self.gamma, self.mu, self.pasos_totales, motor)  # Crea una simulación
            sim.ejecutar(mostrar=False)  # Ejecuta la simulación sin mostrar la grilla
            resumen = sim.obtener_estadisticas() # Obtiene las estadísticas finales de la simulación
            self.resultados.append(resumen) # Almacena los resultados

    # Funcion que calcula el promedio de cada metrica final
    def calcular_promedio(self):

            suma = {
                "pico_infectados": 0,
                "paso_pico": 0,
                "duracion": 0,
                "total_infectados_acumulado": 0
            }

            for r in self.resultados: # Recorre cada resultado de las simulaciones
                for clave in suma: # Recorre cada clave de las métricas a promediar
                    suma[clave] += r[clave] # Suma el valor de la métrica actual al total

            n = len(self.resultados) # Número de simulaciones realizadas

            if n == 0: # si no se realizaron simulaciones, retorna None
                return None
            
            promedio = {} # Diccionario para almacenar los promedios
            for clave in suma: # Recorre cada clave de las métricas
                promedio[clave] = suma[clave] / n # Calcula el promedio dividiendo la suma total por el número de simulaciones

            return promedio # Devuelve el diccionario con los promedios de las métricas finales
    
    # Funcion que imprime el resumen promedio de las simulaciones
    def mostrar_resultado_promedio(self):
        promedio = self.calcular_promedio()
        if promedio is None:
            print("No se realizaron simulaciones.")
            return
        
        # 
        print("\nResultados promedio Monte Carlo ({} simulaciones):".format(self.repeticiones)) # Imprime el número de simulaciones realizadas
        print("Pico infectados promedio:", round(promedio["pico_infectados"], 2)) # Imprime el pico promedio de infectados
        print("Paso del pico promedio:", round(promedio["paso_pico"], 2)) # Imprime el paso promedio en que ocurre el pico
        print("Duración promedio:", round(promedio["duracion"], 2)) # Imprime la duración promedio
        print("Total infectados acumulado promedio:", round(promedio["total_infectados_acumulado"], 2)) # Imprime el total acumulado de infectados promedio




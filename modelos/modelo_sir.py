# Este archivo contiene una implementación discreta del modelo SIR (Susceptibles, Infectados, Recuperados)
# usando el método de Euler, sin usar librerías externas.

"""
    Clase que representa el modelo compartimental SIR:
    S: Susceptibles
    I: Infectados
    R: Recuperados
    Evolución temporal por pasos con método de Euler.
"""

class ModeloSIR:
    def __init__(self, beta, gamma, mu, S0, I0, R0):
        self.beta = beta # Tasa de transmisión
        self.gamma = gamma # Tasa de recuperación
        self.mu = mu # Tasa de mortalidad

        self.S = S0  # Susceptibles iniciales
        self.I = I0 # Infectados iniciales
        self.R = R0 # Recuperados iniciales
        
        self.N = S0 + I0 + R0  # Población total

        self.historial = []  # Historial de estados para análisis posterior, Lista de tuplas (S, I, R)

    """
    Funcion que Calcula el siguiente paso en el tiempo según las ecuaciones del modelo SIR.
    dS/dt = -beta * S * I / N
    dI/dt = beta * S * I / N - gamma * I - mu * I
    dR/dt = gamma * I
    """
    def paso(self):
        dS = -self.beta * self.S * self.I / self.N
        dI = self.beta * self.S * self.I / self.N - self.gamma * self.I - self.mu * self.I
        dR = self.gamma * self.I

        # Avanzamos un paso discreto de tamaño 1
        self.S += dS
        self.I += dI
        self.R += dR

        # Guarda el estado actual en el historial
        self.historial.append((self.S, self.I, self.R))

    # Funcion que ejecuta la simulación por un número de pasos especificado.
    def correr_simulacion(self, pasos):
        for _ in range(pasos): # Repite el proceso por el número de pasos especificado
            self.paso() # Guarda el estado actual en el historial

    # Funcion que retorna el historial de estados.
    def obtener_historial(self):
        return self.historial  # Devuelve el historial de estados (S, I, R) a lo largo del tiempo
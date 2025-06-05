from motor.celda import Celda  # Importamos la clase Celda
from modelos.estado_celda import EstadoCelda  # Importamos la clase EstadoCelda

"""
Esta clase representa una grilla 2d del autómata celular.
Controla la evoluvion de las celdas segun las reglas del modelo epidemiológico.
"""
class Grilla:
    def __init__(self, tamano,beta, gamma, mu, motor_aleatorio):
        self.tamano = tamano # Dimension n x n de la grilla
        # Inicializa una grilla de celdas con el estado inicial 'SUSCEPTIBLE'.
        self.celdas = [[Celda(EstadoCelda.SUSCEPTIBLE) for _ in range(tamano)] for _ in range(tamano)]
        self.beta = beta # Tasa de contagio
        self.gamma = gamma # Tasa de recuperación
        self.mu = mu # Tasa de mortalidad
        self.rng = motor_aleatorio # Motor aleatorio para decisiones estocásticas
    
    # Funcion que infecta la celda central al inicio de la simulación.
    def infectar_central(self):
        centro = self.tamano // 2
        self.celdas[centro][centro].estado = EstadoCelda.INFECTADO  # Infecta la celda central

    # Funcion que retorna una lista con los vecinos validos (moore)
    # Representa la funcion de vecinos Moore, que incluye todos los vecinos adyacentes (8 direcciones).
    def vecinos_moore(self, x, y):
        vecinos = [] # Lista para almacenar vecinos válidos
        for dx in [-1, 0, 1]: # Bucle para recorrer vecinos en el rango -1 a 1 en x
            for dy in [-1, 0, 1]: # Bucle para recorrer vecinos en el rango -1 a 1 en y
                if dx == 0 and dy == 0: # si es la celda misma, no la agregamos
                    continue            # Continúa al siguiente ciclo
                nx = x + dx  # Calcula la coordenada x del vecino
                ny = y + dy  # Calcula la coordenada y del vecino
                if 0 <= nx < self.tamano and 0 <= ny < self.tamano: # si el vecino está dentro de los límites de la grilla entonces
                    vecinos.append(self.celdas[nx][ny])  # Agrega el vecino 
        return vecinos
    
    # Funcion que cuenta el cuantos vecinos estan infectados
    def contar_vecinos_infectados(self, vecinos):
        contador = 0
        for celda in vecinos: # Recorre cada vecino
            # Si la celda está infectada, incrementa el contador
            if celda.esta_infectado():
                contador += 1
        return contador
    
    # Funcion que aplica las reglas de transicion a cada celda segun su estado y vecinos

    def aplicar_reglas(self):
        for x in range(self.tamano): # Recorre cada fila de la grilla
            for y in range(self.tamano): # Recorre cada columna de la grilla
                celda = self.celdas[x][y] # Obtiene la celda actual
                vecinos = self.vecinos_moore(x, y) # Obtiene los vecinos de la celda actual

                if celda.esta_susceptible():
                    k = self.contar_vecinos_infectados(vecinos)  # Cuenta los vecinos infectados
                    prob_infeccion = 1 - (1 - self.beta) ** k  # Calcula la probabilidad de infección mediante la fórmula de probabilidad que es : 1 - (1 - beta) ^ k
                    # Si la celda es susceptible y hay vecinos infectados, decide si se infecta
                    if self.rng.aleatorio() < prob_infeccion:
                        celda.definir_proximo_estado(EstadoCelda.INFECTADO)
                # si la celda es infectada, decide si se recupera o fallece
                elif celda.esta_infectado():
                    if self.rng.aleatorio() < self.mu: # Tasa de mortalidad
                        # Si la celda está infectada y muere, cambia su estado a fallecido
                        celda.definir_proximo_estado(EstadoCelda.FALLECIDO)
                    # Si la celda está infectada y no muere, decide si se recupera
                    elif self.rng.aleatorio() < self.gamma:
                        celda.definir_proximo_estado(EstadoCelda.RECUPERADO)

                else: # Si la celda no es susceptible ni infectada, mantiene su estado actual
                    celda.definir_proximo_estado(celda.estado)  # Mantiene el estado actual si no se cumplen las condiciones

    # Función que Cambia el estado actual de todas las celdas al estado siguiente asignado.
    def actualizar_estados(self):
        for fila in self.celdas: # Recorre cada fila de la grilla
            for celda in fila: # Recorre cada celda en la fila
                celda.actualizar_estado() # Actualiza el estado de la celda al siguiente estado provisional
    
    # Funcion que Cuenta cuántas celdas hay en cada estado.
    # Devuelve un diccionario: {estado: cantidad}
    def contar_por_estado(self):
        # Diccionario para almacenar el conteo de cada estado
        conteo = {
            EstadoCelda.SUSCEPTIBLE: 0,
            EstadoCelda.INFECTADO: 0,
            EstadoCelda.RECUPERADO: 0,
            EstadoCelda.FALLECIDO: 0
        }
        for fila in self.celdas: # Bucle para recorrer cada fila de la grilla
            for celda in fila: # Bucle para recorrer cada celda en la fila
                conteo[celda.estado] += 1 # Incrementa el contador del estado actual de la celda
        return conteo
    
    # Funcion que imprime la grilla actual usanod el simbolo de cada celda.
    def mostrar_consola(self):
        for fila in self.celdas:  # Recorre cada fila de la grilla
            linea = " ".join(celda.simbolo() for celda in fila) # Crea una línea con los símbolos de cada celda en la fila
            print(linea)  # Imprime el símbolo de cada celda en la fila
        print("-")  

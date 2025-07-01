# Esta clase define los posibles estados de una celda.
# No usamos 'enum.Enum' por la restricción de no usar librerías externas.
# Usamos una clase con constantes enteras.

class EstadoCelda:
    SUSCEPTIBLE = 0  # celda, individuo que puede infectarse
    INFECTADO = 1   # celda, individuo que puede contagiar a otros
    RECUPERADO = 2  # celda, individuo que se ha recuperado (inmunizado)
    FALLECIDO = 3    # celda, individuo que ha fallecido

    # Método para obtener el nombre del estado como cadena
    @staticmethod # Método estático que no requiere instancia de la clase
    def a_texto(valor):
        # Convierte el valor entero en una cadena legible para mostrar por consola o exportar.
        if valor == EstadoCelda.SUSCEPTIBLE:
            return "\033["+"7;30;42"+"m "+"\U0001F535" + " \033[0m" # Susceptible
        elif valor == EstadoCelda.INFECTADO:
            return "\033["+"7;30;42"+"m "+"\U0001F7E2" + " \033[0m" # Infectado
        elif valor == EstadoCelda.RECUPERADO:
            return "\033["+"7;30;42"+"m "+"\U000026AA" + " \033[0m" # Recuperado
        elif valor == EstadoCelda.FALLECIDO:
            return "\033["+"7;30;42"+"m "+"\U0001F480" + " \033[0m" # Fallecido
        else:
            return "?" # Estado desconocido
        
    # Funcion que retorna una lista con los estados posibles
    @staticmethod
    
    def lista_estados():
        return [
            EstadoCelda.SUSCEPTIBLE,
            EstadoCelda.INFECTADO,
            EstadoCelda.RECUPERADO,
            EstadoCelda.FALLECIDO
        ]
    # Método para obtener el nombre del estado como cadena
    @staticmethod
    def nombre_estados():
        return [
            "Susceptible",
            "Infectado",
            "Recuperado",
            "Fallecido"
        ]
"""
Este archivo conecta todas las partes del sistema EpiDecide.
Es el punto de entrada para ejecutar la simulación y obtener
resultados con parametros definidos.
"""
from motor.simulacion import Simulacion  # Importa la clase Simulacion desde el módulo motor
from motor.motor_aleatorio import MotorAleatorio  # Importa la clase MotorAleatorio desde el módulo motor_aleatorio

# Parámetros de la simulación
TAMANO_GRILLA = 5  # Tamaño de la grilla (NxN)
BETA = 2.4         # Tasa de transmisión
GAMMA = 0.05        # Tasa de recuperación
MU = 0.01           # Tasa de mortalidad
PASOS = 50          # Número total de pasos a simular
SEMILLA = 12345     # semilla fija para reproducibilidad

# Inicializa el motor aleatorio con una semilla fija
motor_aleatorio = MotorAleatorio(SEMILLA)

# Crear la simulación
simulacion = Simulacion(TAMANO_GRILLA, BETA, GAMMA, MU, PASOS, motor_aleatorio)

# Ejecuta la simulación (True = mostrar grilla por consola)
simulacion.ejecutar(mostrar=True)

# Mostrar resumen final

resumen = simulacion.obtener_estadisticas()
print("\nResumen de la epidemia:")
print("Pico de infectados:", resumen["pico_infectados"])
print("Paso del pico:", resumen["paso_pico"])
print("Duración:", resumen["duracion"])
print("Infectados acumulados:", resumen["total_infectados_acumulado"])

# Exportar el historial (opcional)
historial = simulacion.obtener_historial()

# Guardar en archivo plano -> csv simple
with open("historial_simulacion.csv", "w") as archivo:
    archivo.write("Paso,S,I,R,F\n")  # Encabezados
    for entrada in historial:  # Itera sobre cada entrada del historial
        linea = f"{entrada['paso']},{entrada['S']},{entrada['I']},{entrada['R']},{entrada['F']}\n"
        archivo.write(linea) # Escribe la línea en el archivo

print("Historial guardado en 'historial_simulacion.csv'")  # Mensaje de confirmación
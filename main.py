"""
Este archivo conecta todas las partes del sistema EpiDecide.
Es el punto de entrada para ejecutar la simulación y obtener
resultados con parametros definidos.
"""
from motor.simulacion import Simulacion  # Importa la clase Simulacion desde el módulo motor
from motor.motor_aleatorio import MotorAleatorio  # Importa la clase MotorAleatorio desde el módulo motor_aleatorio

# Parámetros de la simulación
TAMANO_GRILLA = 10  # Tamaño de la grilla (NxN)
BETA = 3       # Tasa de transmisión
GAMMA = 0.05        # Tasa de recuperación
MU = 0.1          # Tasa de mortalidad
PASOS = 10        # Número total de pasos a simular
SEMILLA = 23456     # semilla fija para reproducibilidad

# Inicializa el motor aleatorio con una semilla fija
motor_aleatorio = MotorAleatorio(SEMILLA)

# Crear la simulación
simulacion = Simulacion(TAMANO_GRILLA, BETA, GAMMA, MU, PASOS, motor_aleatorio)

# Ejecuta la simulación (True = mostrar grilla por consola)
simulacion.ejecutar(mostrar=True)

# Mostrar resumen final

resumen = simulacion.obtener_estadisticas()
print("\nResumen de la epidemia:", flush=True)
print("Pico de infectados:", resumen["pico_infectados"], flush=True)
print("Paso del pico:", resumen["paso_pico"], flush=True)
print("Duración:", resumen["duracion"], flush=True)
print("Infectados acumulados:", resumen["total_infectados_acumulado"], flush=True)

# Exportar el historial (opcional)
historial = simulacion.obtener_historial()

# Guardar en archivo plano -> csv simple
with open("historial_simulacion.csv", "w") as archivo:
    archivo.write("Paso,S,I,R,F\n")  # Encabezados
    for entrada in historial:  # Itera sobre cada entrada del historial
        linea = f"{entrada['paso']},{entrada['S']},{entrada['I']},{entrada['R']},{entrada['F']}\n"
        archivo.write(linea) # Escribe la línea en el archivo

print("Historial guardado en 'historial_simulacion.csv'", flush=True)  # Mensaje de confirmación

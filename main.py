"""
Este archivo conecta todas las partes del sistema EpiDecide.
Es el punto de entrada para ejecutar la simulación y obtener
resultados con parametros definidos.
"""
import grafica.menu
from motor.simulacion import Simulacion  # Importa la clase Simulacion desde el módulo motor
from motor.motor_aleatorio import MotorAleatorio  # Importa la clase MotorAleatorio desde el módulo motor_aleatorio
import grafica
# Parámetros de la simulación
grafica.menu.creacion_menu.dibujar()  # Muestra el menú de opciones al usuario1
TAMANO_GRILLA = int(input("\033["+"7;30;42"+"m "+"\U0001F449"+" Ingrese el tamaño de la grilla (NxN):"+" \033[0m"))  # Tamaño de la grilla (NxN)
BETA = float(input("\033["+"7;30;42"+"m "+"\U0001F449"+" Ingrese la tasa de transmisión (0-1): "+" \033[0m"))  # Tasa de transmisión 0 -1
GAMMA = float(input("\033["+"7;30;42"+"m "+"\U0001F449"+" Ingrese la tasa de recuperación (0-1): "+" \033[0m"))  # Tasa de recuperación 0 - 1
MU = float(input("\033["+"7;30;42"+"m "+"\U0001F449"+" Ingrese la tasa de mortalidad (0.1-1): "+" \033[0m"))  # Tasa de mortalidad 0.1 - 1
PASOS = int(input("\033["+"7;30;42"+"m "+"\U0001F449"+" Ingrese el número total de pasos a simular: "+" \033[0m"))  # Número total de pasos a simular 0 - 1
# Inicializa el motor aleatorio con una semilla fija
motor_aleatorio = MotorAleatorio(id(object()))

# Crear la simulación
simulacion = Simulacion(TAMANO_GRILLA, BETA, GAMMA, MU, PASOS, motor_aleatorio)

# Ejecuta la simulación (True = mostrar grilla por consola)
simulacion.ejecutar(mostrar=True)

# Mostrar resumen final

resumen = simulacion.obtener_estadisticas()
print("\033["+"7;30;42"+"m "+"Resumen de la epidemia:" + " \033[0m", flush=True)
print("\033["+"7;30;42"+"m "+"Pico de infectados:" , str (resumen["pico_infectados"]) + " \033[0m", flush=True)
print("\033["+"7;30;42"+"m "+"Paso del pico:" , str (resumen["paso_pico"]) + " \033[0m", flush=True)
print("\033["+"7;30;42"+"m "+"Duración:" , str (resumen["duracion"]) + " \033[0m", flush=True)
print("\033["+"7;30;42"+"m "+"Infectados acumulados:" , str (resumen["total_infectados_acumulado"]) + " \033[0m", flush=True)

# Exportar el historial (opcional)
historial = simulacion.obtener_historial()

# Guardar en archivo plano -> csv simple
with open("historial_simulacion.csv", "w") as archivo:
    archivo.write("Paso,S,I,R,F\n")  # Encabezados
    for entrada in historial:  # Itera sobre cada entrada del historial
        linea = f"{entrada['paso']},{entrada['S']},{entrada['I']},{entrada['R']},{entrada['F']}\n"
        archivo.write(linea) # Escribe la línea en el archivo

print("Historial guardado en 'historial_simulacion.csv'", flush=True)  # Mensaje de confirmación

# Epidecide

# Estructura de archivos definitiva para el proyecto
````
simulador_epidemia/
├── main.py                                # Script principal de ejecución
├── config/
│   └── parametros.py                      # Definición de parámetros epidemiológicos
├── modelos/
│   ├── modelo_sir.py                      # Modelo SIR con método de Euler
│   └── estado_celda.py                    # Definición de estados de salud
├── motor/
│   ├── motor_aleatorio.py                # Generador de números aleatorios
│   ├── celda.py                          # Definición de la clase Celda
│   ├── grilla.py                         # Definición de la clase Grilla (autómata celular)
│   └── simulacion.py                     # Ejecutor principal de simulación
├── estadisticas/
│   └── recolector.py                     # Recolector de estadísticas por paso
├── montecarlo/
│   └── ejecucion.py                      # Ejecutor de simulaciones Monte Carlo
└── tests/
    ├── test_celda.py                     # Pruebas unitarias para la clase Celda
    ├── test_grilla.py                    # Pruebas para la grilla y vecinos
    └── test_sir.py                       # Pruebas para el modelo SIR
````
##  Visualización de resultados (en consola / exportación):
### - Cada paso de la simulación puede imprimir: Paso, S, I, R, F
### - El Recolector guardará la historia en una lista de diccionarios
### - El archivo main.py podrá exportar esa historia a un archivo CSV
### - El desarrollador frontend podrá consumir los datos desde:
###   * consola (print paso a paso)
###  * archivo intermedio CSV o .json
###   * métodos como get_estado_grilla() para representar el autómata

## Nota sobre librerías externas:
### El proyecto NO utiliza enum, random ni math.
### Todo se implementa con estructuras básicas de Python: listas, cadenas, diccionarios, funciones.

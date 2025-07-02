"""
Este archivo conecta todas las partes del sistema EpiDecide.
Es el punto de entrada para ejecutar la simulación y obtener
resultados con parametros definidos.
"""
import grafica.menu
from motor.simulacion import Simulacion
from motor.motor_aleatorio import MotorAleatorio
from montecarlo.ejecucion import EjecutorMonteCarlo

def mostrar_menu_principal():
    print("\n" + "="*40)
    print("Simulación Epidémica - Menú Principal")
    print("="*40)
    print("1) Ejecutar simulación simple")
    print("2) Ejecutar Monte Carlo (múltiples simulaciones)")
    print("0) Salir")
    print("="*40)

def pedir_parametros_simulacion():
    TAMANO_GRILLA = int(input("\033[7;30;42m \U0001F449 Ingrese el tamaño de la grilla (NxN): \033[0m"))
    BETA = float(input("\033[7;30;42m \U0001F449 Ingrese la tasa de transmisión (0-1): \033[0m"))
    GAMMA = float(input("\033[7;30;42m \U0001F449 Ingrese la tasa de recuperación (0-1): \033[0m"))
    MU = float(input("\033[7;30;42m \U0001F449 Ingrese la tasa de mortalidad (0.1-1): \033[0m"))
    PASOS = int(input("\033[7;30;42m \U0001F449 Ingrese el número total de pasos a simular: \033[0m"))
    return TAMANO_GRILLA, BETA, GAMMA, MU, PASOS

def main():
    grafica.menu.creacion_menu.dibujar()  # Muestra el menú gráfico inicial (si tienes)
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            # Simulación simple
            TAMANO_GRILLA, BETA, GAMMA, MU, PASOS = pedir_parametros_simulacion()
            motor_aleatorio = MotorAleatorio(id(object()))
            simulacion = Simulacion(TAMANO_GRILLA, BETA, GAMMA, MU, PASOS, motor_aleatorio)
            simulacion.ejecutar(mostrar=True)

            resumen = simulacion.obtener_estadisticas()
            print("\033[7;30;42m Resumen de la epidemia: \033[0m", flush=True)
            print("\033[7;30;42m Pico de infectados:", resumen["pico_infectados"], "\033[0m", flush=True)
            print("\033[7;30;42m Paso del pico:", resumen["paso_pico"], "\033[0m", flush=True)
            print("\033[7;30;42m Duración:", resumen["duracion"], "\033[0m", flush=True)
            print("\033[7;30;42m Infectados acumulados:", resumen["total_infectados_acumulado"], "\033[0m", flush=True)

            # Guardar historial
            historial = simulacion.obtener_historial()
            with open("historial_simulacion.csv", "w") as archivo:
                archivo.write("Paso,S,I,R,F\n")
                for entrada in historial:
                    linea = f"{entrada['paso']},{entrada['S']},{entrada['I']},{entrada['R']},{entrada['F']}\n"
                    archivo.write(linea)
            print("Historial guardado en 'historial_simulacion.csv'", flush=True)

        elif opcion == "2":
            # Monte Carlo: pedir repeticiones y parámetros
            repeticiones = int(input("\033[7;30;42m \U0001F449 Ingrese el número de simulaciones Monte Carlo: \033[0m"))
            TAMANO_GRILLA, BETA, GAMMA, MU, PASOS = pedir_parametros_simulacion()

            ejecutor = EjecutorMonteCarlo(repeticiones, TAMANO_GRILLA, BETA, GAMMA, MU, PASOS)
            print(f"\nEjecutando Monte Carlo con {repeticiones} simulaciones, por favor espere...")
            ejecutor.ejecutar_todas()
            ejecutor.mostrar_resultado_promedio()

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()


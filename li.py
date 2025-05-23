import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_pasos(expr):
    print("\n🔸 Expresión original:")
    sp.pprint(expr)

    expandida = sp.expand(expr)
    if expandida != expr:
        print("\n🔹 Paso 1: Expansión de la expresión")
        sp.pprint(expandida)
    else:
        print("\n🔹 Paso 1: No se pudo expandir más")

    factorizada = sp.factor(expandida)
    if factorizada != expandida:
        print("\n🔹 Paso 2: Factorización")
        sp.pprint(factorizada)
    else:
        print("\n🔹 Paso 2: No se pudo factorizar")

    simplificada = sp.simplify(expr)
    if simplificada != expr:
        print("\n🔹 Paso 3: Simplificación de fracciones o expresión general")
        sp.pprint(simplificada)
    else:
        print("\n🔹 Paso 3: No se pudo simplificar más")

    cancelada = sp.cancel(expr)
    if cancelada != expr and cancelada != simplificada:
        print("\n🔹 Paso 4: Cancelación de términos comunes")
        sp.pprint(cancelada)

    print("\n Resultado final simplificado:")
    sp.pprint(simplificada)

def simplificar():
    limpiar_pantalla()
    print("SIMPLIFICADOR DE FUNCIONES MATEMÁTICAS")
    print("Ejemplo de entrada: (x**2 + 2*x + 1)/(x + 1)\n")

    entrada = input("➡ Ingresá tu función: ")
    try:
        variables = sp.symbols('x y z a b c')
        expr = parse_expr(entrada, evaluate=False)
        mostrar_pasos(expr)
    except Exception as e:
        print("Error al interpretar la función:", e)

    input("\nPresioná Enter para volver al menú...")

def como_funciona():
    limpiar_pantalla()
    print("¿Cómo funciona el simplificador?\n")
    print("- Este programa usa la biblioteca SymPy para:")
    print("  1. Expandir expresiones algebraicas.")
    print("  2. Factorizar términos comunes.")
    print("  3. Simplificar fracciones algebraicas.")
    print("  4. Cancelar términos si es posible.\n")
    print("Podés usar variables como x, y, z, a, b, c y operadores como +, -, *, / y potencias con **.")
    print("Ejemplo: (x**2 + 2*x + 1)/(x + 1)\n")

    input("Presioná Enter para volver al menú...")

def main():
    while True:
        limpiar_pantalla()
        print("--- Bienvenido al simplificador ---")
        print("1. Simplificar.")
        print("2. Cómo funciona.")
        print("3. Salir.")
        opcion = input("\n🟢 Elegí una opción (1-3): ")

        if opcion == '1':
            simplificar()
        elif opcion == '2':
            como_funciona()
        elif opcion == '3':
            limpiar_pantalla()
            print("¡Gracias por usar el simplificador!")
            break
        else:
            input("Opción no válida. Presioná Enter para intentar de nuevo...")

if __name__ == "__main__":
    main()

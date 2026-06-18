# =============================================================================
# main.py  —  Punto de entrada principal del programa
# Materia : Programación 1 - UTN TUPAD
# Descripción: Menú interactivo que integra todos los módulos del sistema
#              de gestión de países.
# =============================================================================

import os

# --- Importaciones de módulos propios ---
from modulos.archivo_csv  import cargar_paises, guardar_paises
from modulos.gestion      import agregar_pais, actualizar_pais, buscar_pais
from modulos.filtros      import menu_filtros
from modulos.ordenamiento import ordenar_paises
from modulos.estadisticas import mostrar_estadisticas
from modulos.presentacion import mostrar_tabla, mostrar_menu_principal

# Nombre del archivo CSV con los datos base
ARCHIVO_CSV = os.path.join("data", "paises.csv")


def main():
    """
    Función principal del programa.
    Carga los datos desde el CSV, muestra el menú en bucle y
    despacha cada opción a su módulo correspondiente.
    Al elegir la opción 8 guarda los cambios y termina la ejecución.
    """
    # Construir ruta absoluta al CSV en el mismo directorio que este archivo
    directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_csv   = os.path.join(directorio, ARCHIVO_CSV)

    print("=" * 52)
    print("  Iniciando sistema... cargando datos.")
    try:
        paises = cargar_paises(ruta_csv)
    except (FileNotFoundError, PermissionError, UnicodeError, RuntimeError, ValueError) as e:
        print(f"[ERROR] {e}")
        paises = []
    print(f"  {len(paises)} países cargados desde '{ARCHIVO_CSV}'.")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-8): ").strip()

        try:
            if opcion == "1":
                agregar_pais(paises)
            elif opcion == "2":
                actualizar_pais(paises)
            elif opcion == "3":
                buscar_pais(paises)
            elif opcion == "4":
                menu_filtros(paises)
            elif opcion == "5":
                ordenar_paises(paises)
            elif opcion == "6":
                mostrar_estadisticas(paises)
            elif opcion == "7":
                mostrar_tabla(paises, "Todos los países")
            elif opcion == "8":
                guardar_paises(paises, ruta_csv)
                print("¡Hasta luego!")
                break
            else:
                print("[ERROR] Opción inválida. Ingrese un número del 1 al 8.")
        except (LookupError, ValueError, PermissionError, RuntimeError) as e:
            print(f"[ERROR] {e}")


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()

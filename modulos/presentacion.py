# =============================================================================
# modulos/presentacion.py
# Responsabilidad: mostrar datos en consola (tabla y menú principal).
# =============================================================================


def mostrar_tabla(paises, titulo="Países"):
    """
    Muestra una lista de países en formato tabular con cabecera.
    Si la lista está vacía, informa al usuario.
    """
    print(f"\n  {titulo}")

    if not paises:
        print("  (Sin resultados para mostrar)")
        return

    encabezado = f"  {'#':<4} {'Nombre':<35} {'Población':>16} {'Superficie (km²)':>18} {'Continente'}"
    separador  = "  " + "─" * 85
    print(encabezado)
    print(separador)

    for i, pais in enumerate(paises, start=1):
        print(f"  {i:<4} {pais['nombre']:<35} {pais['poblacion']:>16,} {pais['superficie']:>18,}  {pais['continente']}")

    print(separador)
    print(f"  Total: {len(paises)} país/es.\n")


def mostrar_menu_principal():
    """Imprime el menú principal de opciones en consola."""
    print("\n" + "═" * 52)
    print("    GESTIÓN DE PAÍSES  ·  Programación 1 · UTN")
    print("═" * 52)
    print("  1. Agregar un país")
    print("  2. Actualizar datos de un país")
    print("  3. Buscar país por nombre")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Ver estadísticas")
    print("  7. Mostrar todos los países")
    print("  8. Guardar cambios y salir")
    print("═" * 52)

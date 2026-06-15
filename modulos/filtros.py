# =============================================================================
# modulos/filtros.py
# Responsabilidad: filtrar países por continente, población o superficie.
# =============================================================================

from modulos.validaciones import pedir_texto_no_vacio, pedir_entero_positivo, normalizar_continente
from modulos.presentacion import mostrar_tabla


def filtrar_por_continente(paises):
    """Muestra únicamente los países que pertenecen al continente indicado."""
    print("\n── Filtrar por Continente ────────────────────")
    while True:
        entrada = pedir_texto_no_vacio("Continente: ")
        try:
            continente = normalizar_continente(entrada)
            if continente is None:
                raise LookupError("Continente no reconocido. Opciones: África, América, Asia, Europa, Oceanía, Antártida.")
            break
        except LookupError as e:
            print(f"[ERROR] {e}")

    resultados = [p for p in paises if p["continente"] == continente]
    mostrar_tabla(resultados, f"Países en '{continente}'")


def filtrar_por_rango_poblacion(paises):
    """Muestra países cuya población se encuentre dentro del rango ingresado."""
    print("\n── Filtrar por Rango de Población ───────────")
    minimo = pedir_entero_positivo("Población mínima: ")
    maximo = pedir_entero_positivo("Población máxima: ")

    if minimo > maximo:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo.")
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    mostrar_tabla(resultados, f"Países con población entre {minimo:,} y {maximo:,} hab.")


def filtrar_por_rango_superficie(paises):
    """Muestra países cuya superficie en km² se encuentre dentro del rango ingresado."""
    print("\n── Filtrar por Rango de Superficie ──────────")
    minimo = pedir_entero_positivo("Superficie mínima (km²): ")
    maximo = pedir_entero_positivo("Superficie máxima (km²): ")

    if minimo > maximo:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo.")
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    mostrar_tabla(resultados, f"Países con superficie entre {minimo:,} y {maximo:,} km²")


def menu_filtros(paises):
    """Submenú que agrupa las tres opciones de filtrado disponibles."""
    while True:
        print("\n" + "═" * 52)
        print("    FILTRAR PAÍSES")
        print("═" * 52)
        print("  1. Por continente")
        print("  2. Por rango de población")
        print("  3. Por rango de superficie")
        print("  4. Volver")
        print("═" * 52)

        opcion = input("Seleccione filtro: ").strip()
        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(paises)
        elif opcion == "4":
            break
        else:
            print("[ERROR] Opción inválida. Elija entre 1 y 4.")

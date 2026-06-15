# =============================================================================
# modulos/estadisticas.py
# Responsabilidad: calcular y mostrar estadísticas del dataset de países.
# =============================================================================

import operator


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales del dataset:
    - País con mayor y menor población.
    - Promedio de población y de superficie.
    - Cantidad de países por continente.
    """
    print("\n── Estadísticas ──────────────────────────────")

    if not paises:
        print("[AVISO] No hay países cargados para calcular estadísticas.")
        return

    total = len(paises)

    # País con mayor y menor población
    pais_max_pob = max(paises, key=operator.itemgetter("poblacion"))
    pais_min_pob = min(paises, key=operator.itemgetter("poblacion"))

    # Promedios
    promedio_pob = sum(p["poblacion"]  for p in paises) / total
    promedio_sup = sum(p["superficie"] for p in paises) / total

    # Cantidad de países por continente usando un diccionario de contadores
    por_continente = {}
    for pais in paises:
        continente = pais["continente"]
        por_continente[continente] = por_continente.get(continente, 0) + 1

    # Presentación de resultados
    print(f"\n  Total de países cargados : {total}")
    print(f"\n  Mayor población  : {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,} hab.)")
    print(f"  Menor población  : {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,} hab.)")
    print(f"\n  Promedio de población  : {promedio_pob:>15,.0f} hab.")
    print(f"  Promedio de superficie : {promedio_sup:>15,.0f} km²")
    print("\n  Cantidad de países por continente:")

    for continente in sorted(por_continente):
        cantidad = por_continente[continente]
        barra = "█" * cantidad
        print(f"    {continente:<30} {cantidad:>3}  {barra}")

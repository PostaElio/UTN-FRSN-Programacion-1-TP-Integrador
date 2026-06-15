# =============================================================================
# modulos/busqueda.py
# Responsabilidad: búsqueda de países por nombre (parcial y exacta).
# =============================================================================

from modulos.validaciones import pedir_texto_no_vacio
from modulos.presentacion import mostrar_tabla


def buscar_exacto(paises, nombre):
    """
    Búsqueda por nombre exacto (sin distinción de mayúsculas/minúsculas).
    Retorna el diccionario del país o None si no se encuentra.
    Usada internamente por gestion.py para evitar duplicados y localizar países.
    """
    nombre_lower = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_lower:
            return pais
    return None


def buscar_pais(paises):
    """
    Busca países cuyo nombre contenga el texto ingresado (coincidencia parcial).
    La búsqueda no distingue mayúsculas de minúsculas.
    """
    print("\n── Buscar País por Nombre ────────────────────")
    termino = pedir_texto_no_vacio("Ingrese nombre o parte del nombre: ")

    resultados = [p for p in paises if termino.lower() in p["nombre"].lower()]
    mostrar_tabla(resultados, f"Resultados para '{termino}'")

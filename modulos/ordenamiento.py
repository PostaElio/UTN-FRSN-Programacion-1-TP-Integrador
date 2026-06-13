# =============================================================================
# modulos/ordenamiento.py
# Responsabilidad: ordenar la lista de países según distintos criterios.
# =============================================================================

import operator

from modulos.validaciones import pedir_direccion_orden
from modulos.presentacion import mostrar_tabla


def _clave_nombre(p):
    return p["nombre"].lower()


def ordenar_paises(paises):
    """
    Permite ordenar la lista por nombre, población o superficie,
    en dirección ascendente o descendente, sin modificar la lista original.
    """
    print("\n── Ordenar Países ────────────────────────────")
    print("  1. Por nombre")
    print("  2. Por población")
    print("  3. Por superficie")

    criterios = {
        "1": ("nombre",     "Nombre"),
        "2": ("poblacion",  "Población"),
        "3": ("superficie", "Superficie"),
    }

    opcion = input("Criterio de ordenamiento: ").strip()
    if opcion not in criterios:
        print("[ERROR] Opción inválida. Elija entre 1 y 3.")
        return

    campo, etiqueta = criterios[opcion]
    descendente = pedir_direccion_orden()

    # Para el campo nombre se ordena en minúsculas para ignorar mayúsculas
    if campo == "nombre":
        ordenados = sorted(paises, key=_clave_nombre, reverse=descendente)
    else:
        ordenados = sorted(paises, key=operator.itemgetter(campo), reverse=descendente)

    direccion_texto = "descendente" if descendente else "ascendente"
    mostrar_tabla(ordenados, f"Países ordenados por {etiqueta} ({direccion_texto})")

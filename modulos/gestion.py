# =============================================================================
# modulos/gestion.py
# Responsabilidad: agregar nuevos países y actualizar datos existentes.
# =============================================================================

from modulos.validaciones import pedir_texto_no_vacio, pedir_entero_positivo, normalizar_continente
from modulos.busqueda     import buscar_exacto


def agregar_pais(paises):
    """
    Solicita los datos de un nuevo país y lo agrega a la lista.
    No permite nombres duplicados ni campos vacíos.
    """
    print("\n── Agregar País ──────────────────────────────")
    nombre = pedir_texto_no_vacio("Nombre del país  : ")

    # Evitar duplicados (comparación sin distinguir mayúsculas)
    if buscar_exacto(paises, nombre) is not None:
        raise LookupError(f"Ya existe un país llamado '{nombre}'.") 

    poblacion  = pedir_entero_positivo("Población        : ")
    superficie = pedir_entero_positivo("Superficie (km²) : ")
    while True:
        entrada = pedir_texto_no_vacio("Continente       : ")
        try:
            continente = normalizar_continente(entrada)
            if continente is None:
                raise LookupError("Continente no reconocido. Opciones: África, América, Asia, Europa, Oceanía, Antártida.")
            break
        except LookupError as e:
            print(f"[ERROR] {e}")

    paises.append({
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"[OK] País '{nombre}' agregado exitosamente.")


def actualizar_pais(paises):
    """
    Busca un país por nombre exacto y permite modificar su población y superficie.
    Solo se actualizan esos dos campos (el nombre y el continente permanecen igual).
    """
    print("\n── Actualizar País ───────────────────────────")
    nombre = pedir_texto_no_vacio("Nombre del país a actualizar: ")

    pais = buscar_exacto(paises, nombre)
    if pais is None:
        raise LookupError(f"No se encontró ningún país llamado '{nombre}'.")

    print(f"  Datos actuales → Población: {pais['poblacion']:,} hab.  |  Superficie: {pais['superficie']:,} km²")
    pais["poblacion"]  = pedir_entero_positivo("Nueva población        : ")
    pais["superficie"] = pedir_entero_positivo("Nueva superficie (km²) : ")
    print(f"[OK] País '{pais['nombre']}' actualizado exitosamente.")

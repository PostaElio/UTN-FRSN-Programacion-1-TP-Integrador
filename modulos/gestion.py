# =============================================================================
# modulos/gestion.py
# Responsabilidad: búsqueda, alta y modificación de países.
# =============================================================================

from modulos.validaciones import pedir_texto_no_vacio, pedir_entero_positivo, normalizar_continente
from modulos.presentacion import mostrar_tabla


def buscar_exacto(paises, nombre):
    """
    Búsqueda por nombre exacto (sin distinción de mayúsculas/minúsculas).
    Retorna el diccionario del país o None si no se encuentra.
    Usada internamente para evitar duplicados y localizar países.
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

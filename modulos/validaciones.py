# =============================================================================
# modulos/validaciones.py
# Responsabilidad: funciones de entrada y validación de datos del usuario.
# =============================================================================

import unicodedata

# Mapa de variantes → nombre canónico
_CONTINENTES = {
    "africa":        "África",
    "america":       "América",
    "asia":          "Asia",
    "europa":        "Europa",
    "oceania":       "Oceanía",
    "antartida":     "Antártida",
}


def _sin_tildes(texto):
    """Convierte a minúsculas y elimina tildes/diacríticos para comparación."""
    normalizado = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def _es_texto_alfabetico(texto):
    """Valida que el texto contenga solo letras y espacios."""
    return all(parte.isalpha() for parte in texto.split())


def normalizar_continente(texto):
    """
    Devuelve el nombre canónico del continente o None si no se reconoce.
    Ejemplo: 'america', 'América', 'AMERICA' → 'América'
    """
    clave = _sin_tildes(texto.strip())
    return _CONTINENTES.get(clave)



def pedir_texto_no_vacio(mensaje):
    """Solicita una cadena de texto no vacía. Repite hasta obtener un valor válido."""
    while True:
        valor = input(mensaje).strip()
        try:
            if not valor:
                raise ValueError("Este campo no puede estar vacío.")
            if not _es_texto_alfabetico(valor):
                raise ValueError("Ingrese solo letras y espacios.")
            return valor
        except ValueError as e:
            print(f"[ERROR] {e}")


def pedir_entero_positivo(mensaje):
    """Solicita un número entero mayor o igual a cero. Repite hasta obtener un valor válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            try:
                numero = int(entrada)
            except ValueError:
                raise ValueError("Ingrese un número entero válido (sin decimales ni letras).")
            if numero < 0:
                raise ValueError("El valor debe ser mayor o igual a 0.")
            return numero
        except ValueError as e:
            print(f"[ERROR] {e}")


def pedir_direccion_orden():
    """
    Solicita la dirección de ordenamiento (ascendente o descendente).
    Retorna True si es descendente, False si es ascendente.
    """
    while True:
        entrada = input("Dirección (asc / desc): ").strip().lower()
        try:
            if entrada not in ("asc", "desc"):
                raise ValueError("Ingrese 'asc' para ascendente o 'desc' para descendente.")
            return entrada == "desc"
        except ValueError as e:
            print(f"[ERROR] {e}")

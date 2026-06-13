# =============================================================================
# modulos/archivo_csv.py
# Responsabilidad: lectura y escritura del archivo CSV de países.
# =============================================================================

import csv
import os

from modulos.validaciones import normalizar_continente

# Nombres de las columnas que debe tener el CSV
CAMPOS_CSV = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta):
    """
    Lee el archivo CSV indicado y retorna una lista de diccionarios,
    uno por cada país válido encontrado.
    Maneja errores de archivo no encontrado, permisos y formato incorrecto.
    """
    paises = []

    if not os.path.exists(ruta):
        print(f"[AVISO] No se encontró '{ruta}'. Se iniciará con lista vacía.")
        return paises

    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            # Verificar que el CSV tenga las columnas esperadas
            if lector.fieldnames is None or not all(c in lector.fieldnames for c in CAMPOS_CSV):
                columnas_requeridas = ", ".join(CAMPOS_CSV)
                print(f"[ERROR] El CSV no tiene las columnas requeridas ({columnas_requeridas}).")
                return paises

            for numero_linea, fila in enumerate(lector, start=2):
                pais = _parsear_fila(fila, numero_linea)
                if pais is not None:
                    paises.append(pais)

    except PermissionError:
        print(f"[ERROR] Sin permiso para leer '{ruta}'.")
    except UnicodeDecodeError:
        print("[ERROR] El archivo no está codificado en UTF-8.")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")

    return paises


def _parsear_fila(fila, numero_linea):
    """
    Convierte una fila del CSV en un diccionario con los tipos correctos.
    Retorna None si la fila contiene errores de formato o campos vacíos.
    (Función privada, usada solo internamente por cargar_paises)
    """
    try:
        nombre     = fila.get("nombre",     "").strip()
        continente_raw = fila.get("continente", "").strip()

        if not nombre or not continente_raw:
            print(f"[AVISO] Línea {numero_linea}: campo vacío, fila omitida.")
            return None

        continente = normalizar_continente(continente_raw)
        if continente is None:
            print(f"[AVISO] Línea {numero_linea}: continente '{continente_raw}' no reconocido, fila omitida.")
            return None

        poblacion  = int(fila.get("poblacion",  "").strip())
        superficie = int(fila.get("superficie", "").strip())

        if poblacion < 0 or superficie < 0:
            print(f"[AVISO] Línea {numero_linea}: valores negativos, fila omitida.")
            return None

        return {
            "nombre":     nombre,
            "poblacion":  poblacion,
            "superficie": superficie,
            "continente": continente
        }

    except ValueError:
        print(f"[AVISO] Línea {numero_linea}: formato numérico inválido, fila omitida.")
        return None


def guardar_paises(paises, ruta):
    """
    Guarda la lista de países en el archivo CSV, sobreescribiendo el contenido anterior.
    Incluye la cabecera con los nombres de columna.
    """
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_CSV)
            escritor.writeheader()
            escritor.writerows(paises)
        print("[OK] Datos guardados correctamente.")
    except PermissionError:
        print(f"[ERROR] Sin permiso para escribir en '{ruta}'.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")

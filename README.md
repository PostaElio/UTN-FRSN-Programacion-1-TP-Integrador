# Trabajo Práctico Integrador - Gestión de Países

## Datos institucionales

- Universidad: Universidad Tecnológica Nacional
- Regional: Facultad Regional San Nicolás
- Carrera: Tecnicatura Universitaria en Programación
- Materia: Programación 1
- Grupo: 77
- Año: 2026

### Integrantes

- Lautaro Villalobos - Comisión 26
- Elio Posta - Comisión 23

### Docentes

- Coordinador: Alberto Cortez
- Profesores: 
  - Ariel Enferrel
  - Martín A. García
  - Cinthia Rigoni
- Tutores:
	- Martina Zabala - Comisión 26
	- Juan Sarmiento - Comisión 23

## Descripción del proyecto

Este proyecto consiste en una aplicación de consola desarrollada en Python para la gestión de información de países. Permite cargar datos desde un archivo CSV, agregar nuevos registros, actualizar información existente, realizar búsquedas, aplicar filtros, ordenar resultados y mostrar estadísticas generales.

El sistema fue pensado como trabajo práctico integrador de la materia Programación 1, con una estructura modular orientada a separar responsabilidades y facilitar el mantenimiento del código.

## Resumen de funcionamiento

Al iniciar el programa, el sistema carga desde `data/paises.csv` la información disponible de países en memoria. A partir de esa carga inicial, el usuario interactúa con un menú principal desde consola que permite agregar nuevos países, actualizar registros existentes, buscar coincidencias por nombre, aplicar filtros, ordenar resultados y consultar estadísticas.

Cada opción del menú deriva el trabajo a un módulo específico, lo que permite separar la lectura y escritura del archivo, las validaciones de entrada, la gestión de datos, la presentación en pantalla y el procesamiento de búsquedas, filtros y ordenamientos. Cuando el usuario elige salir, el sistema guarda los cambios realizados en el archivo CSV para conservar la información actualizada.

## Estructura del proyecto

```text
UTN-FRSN-Programacion-1-TP-Integrador/
├── main.py
├── README.md
├── data/
│   └── paises.csv
└── modulos/
	├── __init__.py
	├── archivo_csv.py
	├── busqueda.py
	├── estadisticas.py
	├── filtros.py
	├── gestion.py
	├── ordenamiento.py
	├── presentacion.py
	└── validaciones.py
```

## Descripción de módulos

- `main.py`: punto de entrada del programa y menú principal.
- `data/paises.csv`: archivo de persistencia inicial con los datos de países.
- `modulos/archivo_csv.py`: lectura y escritura del archivo CSV.
- `modulos/busqueda.py`: búsqueda exacta y parcial de países.
- `modulos/estadisticas.py`: cálculo y visualización de estadísticas.
- `modulos/filtros.py`: filtros por continente, población y superficie.
- `modulos/gestion.py`: alta y actualización de países.
- `modulos/ordenamiento.py`: ordenamiento por distintos criterios.
- `modulos/presentacion.py`: impresión de menús y tablas en consola.
- `modulos/validaciones.py`: validaciones de entrada y normalización de datos.

## Instrucciones de ejecución

### Requisitos

- Python 3.10 o superior recomendado.
- Consola compatible con ejecución de scripts Python.

### Pasos para ejecutar

1. Abrir una terminal en la carpeta raíz del proyecto.
2. Ejecutar el programa con:

```bash
py main.py
```

Si el comando `py` no está disponible en tu entorno, también podés usar:

```bash
python main.py
```

## Uso de librerías de terceros

Este proyecto no utiliza librerías externas de terceros.

Solo emplea módulos estándar de Python:

- `os`
- `csv`
- `unicodedata`
- `operator`

## Funcionalidades principales

- Carga de datos desde archivo CSV.
- Alta de nuevos países.
- Actualización de población y superficie.
- Búsqueda por nombre.
- Filtro por continente.
- Filtro por rango de población.
- Filtro por rango de superficie.
- Ordenamiento por nombre, población o superficie.
- Visualización de estadísticas.
- Guardado de cambios en el archivo CSV.

## Ejemplo de uso

### 1. Agregar un país

```text
Seleccione una opción (1-8): 1
Nombre del país  : Argentina
Población        : 45376763
Superficie (km²) : 2780400
Continente       : america
[OK] País 'Argentina' agregado exitosamente.
```

### 2. Actualizar datos de un país

```text
Seleccione una opción (1-8): 2
Nombre del país a actualizar: Argentina
Datos actuales → Población: 45,376,763 hab.  |  Superficie: 2,780,400 km²
Nueva población        : 46234830
Nueva superficie (km²) : 2780400
[OK] País 'Argentina' actualizado exitosamente.
```

### 3. Buscar país por nombre

```text
Seleccione una opción (1-8): 3
Ingrese nombre o parte del nombre: arg

Resultados para 'arg'
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Argentina                              46,234,830          2,780,400  América
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 1 país/es.
```

### 4. Filtrar países

#### Filtrar por continente

```text
Seleccione una opción (1-8): 4
Seleccione filtro: 1
Continente: europa

Países en 'Europa'
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    España                                  48,345,223            505,990  Europa
	2    Francia                                 68,373,433            551,695  Europa
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 2 país/es.
```

#### Filtrar por rango de población

```text
Seleccione una opción (1-8): 4
Seleccione filtro: 2
Población mínima: 10000000
Población máxima: 50000000

Países con población entre 10,000,000 y 50,000,000 hab.
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Argentina                              46,234,830          2,780,400  América
	2    España                                  48,345,223            505,990  Europa
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 2 país/es.
```

#### Filtrar por rango de superficie

```text
Seleccione una opción (1-8): 4
Seleccione filtro: 3
Superficie mínima (km²): 500000
Superficie máxima (km²): 3000000

Países con superficie entre 500,000 y 3,000,000 km²
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Argentina                              46,234,830          2,780,400  América
	2    Francia                                 68,373,433            551,695  Europa
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 2 país/es.
```

### 5. Ordenar países

Al seleccionar esta opción, el sistema muestra el siguiente submenú:

```text
── Ordenar Países ────────────────────────────
	1. Por nombre
	2. Por población
	3. Por superficie
```

#### Ordenar por nombre

```text
Seleccione una opción (1-8): 5
Criterio de ordenamiento: 1
Dirección (asc / desc): asc

Países ordenados por Nombre (ascendente)
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Argentina                              46,234,830          2,780,400  América
	2    Brasil                                203,080,756          8,515,767  América
	3    España                                 48,345,223            505,990  Europa
	4    Uruguay                                 3,499,451            176,215  América
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 4 país/es.
```

#### Ordenar por población

```text
Seleccione una opción (1-8): 5
Criterio de ordenamiento: 2
Dirección (asc / desc): desc

Países ordenados por Población (descendente)
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Brasil                                203,080,756          8,515,767  América
	2    España                                 48,345,223            505,990  Europa
	3    Argentina                              46,234,830          2,780,400  América
	4    Uruguay                                 3,499,451            176,215  América
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 4 país/es.
```

#### Ordenar por superficie

```text
Seleccione una opción (1-8): 5
Criterio de ordenamiento: 3
Dirección (asc / desc): asc

Países ordenados por Superficie (ascendente)
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Uruguay                                 3,499,451            176,215  América
	2    España                                 48,345,223            505,990  Europa
	3    Argentina                              46,234,830          2,780,400  América
	4    Brasil                                203,080,756          8,515,767  América
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 4 país/es.
```

### 6. Ver estadísticas

```text
Seleccione una opción (1-8): 6

Total de países cargados : 4

Mayor población  : Brasil (203,080,756 hab.)
Menor población  : Uruguay (3,499,451 hab.)

Promedio de población  :      75,475,857 hab.
Promedio de superficie :       2,286,654 km²

Cantidad de países por continente:
	América                         3  ███
	Europa                          1  █
```

### 7. Mostrar todos los países

```text
Seleccione una opción (1-8): 7

Todos los países
	#    Nombre                                  Población   Superficie (km²) Continente
	─────────────────────────────────────────────────────────────────────────────────────
	1    Argentina                              46,234,830          2,780,400  América
	2    Brasil                                203,080,756          8,515,767  América
	3    España                                 48,345,223            505,990  Europa
	4    Uruguay                                 3,499,451            176,215  América
	─────────────────────────────────────────────────────────────────────────────────────
	Total: 4 país/es.
```

### 8. Guardar cambios y salir

```text
Seleccione una opción (1-8): 8
¡Hasta luego!
```

### Ejemplo de validación

En este sistema, las validaciones se apoyan en excepciones para separar el flujo normal del flujo de error.

- Se utiliza `raise` para lanzar una excepción cuando un dato no cumple una regla de validación.
- Se utiliza `try/except` para capturar esa excepción, mostrar un mensaje claro al usuario y permitir que el programa continúe funcionando.

### Caso 1. Opción inválida en el submenú de filtros

```text
Seleccione una opción (1-8): 4
════════════════════════════════════════════════════
		FILTRAR PAÍSES
════════════════════════════════════════════════════
	1. Por continente
	2. Por rango de población
	3. Por rango de superficie
	4. Volver
════════════════════════════════════════════════════
Seleccione filtro: 9
[ERROR] Opción inválida. Elija entre 1 y 4.
```

Esto ocurre porque el submenú de filtros solo acepta las opciones `1`, `2`, `3` o `4`. Si el usuario ingresa otro valor, el sistema detecta que la opción no existe y muestra el error correspondiente.

### Caso 2. Campo de texto vacío

```text
Seleccione una opción (1-8): 1
Nombre del país  :
[ERROR] Este campo no puede estar vacío.
```

Esto ocurre porque el nombre del país es obligatorio. En la función de validación se usa `raise ValueError` cuando el texto ingresado está vacío, y luego esa excepción se captura con `try/except` para informar el problema sin cerrar el programa.

### Caso 3. Texto con números o símbolos donde solo se admiten letras

```text
Seleccione una opción (1-8): 1
Nombre del país  : Arg3ntina
[ERROR] Ingrese solo letras y espacios.
```

Esto ocurre porque el sistema valida que los campos de texto contengan únicamente letras y espacios. Si encuentra números o caracteres no válidos, se lanza una excepción con `raise ValueError` y se la maneja inmediatamente con `try/except` dentro de la validación.

### Caso 4. Número entero inválido

```text
Seleccione una opción (1-8): 1
Población        : 45.7
[ERROR] Ingrese un número entero válido (sin decimales ni letras).
```

Esto ocurre porque la población y la superficie deben ingresarse como números enteros. Cuando el sistema intenta convertir el valor a `int` y falla, captura ese error y vuelve a lanzar otro más descriptivo usando `raise ValueError(...)` para que el usuario reciba un mensaje claro.

### Caso 5. Número negativo

```text
Seleccione una opción (1-8): 1
Superficie (km²) : -30
[ERROR] El valor debe ser mayor o igual a 0.
```

Esto ocurre porque no se admiten valores negativos para población ni superficie. Después de convertir el dato a entero, el sistema verifica si es menor que cero y, si lo es, ejecuta `raise ValueError`. Esa excepción se captura con `try/except` y se vuelve a pedir el dato.

### Caso 6. Continente no reconocido

```text
Seleccione una opción (1-8): 1
Continente       : Atlantico
[ERROR] Continente no reconocido. Opciones: África, América, Asia, Europa, Oceanía, Antártida.
```

Esto ocurre porque el continente ingresado no coincide con ninguna de las opciones válidas. En este caso, el sistema usa `normalizar_continente(...)` para intentar reconocer el valor y, si no puede hacerlo, ejecuta `raise LookupError`. Luego el `try/except` muestra el mensaje y permite reintentar.

### Caso 7. País duplicado

```text
Seleccione una opción (1-8): 1
Nombre del país  : Argentina
[ERROR] Ya existe un país llamado 'Argentina'.
```

Esto ocurre porque el sistema no permite agregar un país ya existente. La función de gestión verifica si el nombre ya está cargado y, en ese caso, usa `raise LookupError` para cortar la operación y avisar el problema.

### Caso 8. País inexistente al actualizar

```text
Seleccione una opción (1-8): 2
Nombre del país a actualizar: Wakanda
[ERROR] No se encontró ningún país llamado 'Wakanda'.
```

Esto ocurre porque la actualización requiere que el país exista previamente. Si la búsqueda exacta no encuentra coincidencias, se lanza una excepción con `raise LookupError`, que luego es capturada en el flujo principal del programa.

### Caso 9. Rango inválido en filtros numéricos

```text
Seleccione una opción (1-8): 4
Seleccione filtro: 2
Población mínima: 50000000
Población máxima: 10000000
[ERROR] El valor mínimo no puede ser mayor que el máximo.
```

Esto ocurre porque el valor mínimo debe ser menor o igual que el máximo. Si el orden del rango es incorrecto, el sistema usa `raise ValueError` para impedir un filtro inconsistente.

### Caso 10. Dirección de ordenamiento inválida

```text
Seleccione una opción (1-8): 5
Criterio de ordenamiento: 1
Dirección (asc / desc): arriba
[ERROR] Ingrese 'asc' para ascendente o 'desc' para descendente.
```

Esto ocurre porque el módulo de ordenamiento solo acepta `asc` o `desc` como dirección. Si el usuario escribe otro valor, la validación lanza una excepción con `raise ValueError` y el `try/except` evita que el programa falle.

### Cómo se manejan estas excepciones en el proyecto

- En las funciones de validación, como las que piden texto, números o dirección de ordenamiento, se usa `raise` para generar errores controlados cuando el dato es inválido.
- En varios casos, esas mismas funciones tienen un bloque `try/except` interno para capturar la excepción, mostrar `[ERROR] ...` y volver a pedir el dato al usuario.
- En errores de lógica de negocio, como país duplicado, país inexistente o rango inválido, la excepción se propaga hasta `main.py`, donde el programa la captura con `except (LookupError, ValueError, PermissionError, RuntimeError) as e:`.
- Gracias a este enfoque, el sistema no se detiene ante una entrada incorrecta: informa el problema, conserva el control del flujo y permite seguir usando la aplicación.

## Video de presentación

- Link al video: https://drive.google.com/file/d/1TOBSjV9_GFTXt87dGR_db6Pq26wK0Z2M/view?usp=sharing

## Repositorio GitHub

- Link al repositorio: https://github.com/PostaElio/UTN-FRSN-Programacion-1-TP-Integrador
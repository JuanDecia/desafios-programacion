# 📚 Manejo de Tuplas en Python

## 📌 Definición

Una tupla es una estructura de datos en Python similar a una lista, pero con dos diferencias clave:

* Es inmutable: No se puede modificar después de su creación.

* Sintaxis con paréntesis: Se define con ( ), aunque los paréntesis son opcionales.

## 🔹 Ventajas:
✔ Más eficiente en memoria que las listas.
✔ Útil para datos constantes (ej: días de la semana, coordenadas).
✔ Puede usarse como clave en diccionarios (a diferencia de las listas).

## 🔍 Ejemplo Práctico

```python
    # Definición de tuplas
    tupla1 = (1, 2, 3, 4)  # Con paréntesis
    tupla2 = 5, 6, 7, 8     # Sin paréntesis (válido)
    print("Tupla 1:", tupla1)  # (1, 2, 3, 4)
    print("Tupla 2:", tupla2)  # (5, 6, 7, 8)

    # Acceso a elementos (indexación igual que las listas)
    print("Primer elemento:", tupla1[0])  # 1
    print("Último elemento:", tupla2[-1])  # 8

    # Slicing en tuplas (funciona igual que en listas)
    print("Subtupla [1:3]:", tupla1[1:3])  # (2, 3)

    # Las tuplas son inmutables (esto dará error)
    try:
        tupla1[0] = 10  # TypeError: 'tuple' object does not support item assignment
    except TypeError as e:
        print("Error:", e)

    # Empaquetado y desempaquetado de tuplas
    x, y, z = (10, 20, 30)
    print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

    # Uso en diccionarios (como clave)
    coordenadas = {(1, 2): "Punto A", (3, 4): "Punto B"}
    print("Valor en (1, 2):", coordenadas[(1, 2)])  # "Punto A"
```

## 📌 Operaciones Comunes con Tuplas

Operación	Ejemplo	Resultado
Creación	t = (1, 2, 3)	(1, 2, 3)
Acceso por índice	t[0]	1
Slicing	t[1:3]	(2, 3)
Concatenación	t + (4, 5)	(1, 2, 3, 4, 5)
Repetición	t * 2	(1, 2, 3, 1, 2, 3)
Búsqueda	3 in t	True

### 🚀 ¿Cuándo Usar Tuplas?

✔ Datos inmutables: Ej. constantes, configuraciones.
✔ Claves en diccionarios: Las listas no son válidas como claves.
✔ Retorno múltiple en funciones:

```python
    def min_max(lista):
        return min(lista), max(lista)  # Retorna una tupla

    resultado = min_max([5, 2, 9, 1])
    print(resultado)  # (1, 9)    
```

### 📌 ¿Cómo Probar el Código?

* Copia el código en un archivo 'manipulacion_tuplas.py'.

* Ejecútalo con python manipulacion_tuplas.py.

* Experimenta modificando las operaciones.

### Contribuciones

Las sugerencias y mejoras son bienvenidas. Abre un issue o envía un pull request.
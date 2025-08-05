# Desafío de Manipulación de sublistas

## Descripción
Este repositorio contiene un ejemplo práctico de cómo manipular sublistas en Python, demostrando diferentes técnicas de slicing y reemplazo de elementos.

## 📌 Definición
Las sublistas (o slicing en inglés) son una técnica en Python que permite extraer, modificar o reemplazar segmentos de una lista utilizando índices. La sintaxis básica es:

```python
    lista[inicio:fin:paso]
```

* inicio (opcional): Índice donde comienza el corte (incluido). Si se omite, empieza desde el principio.

* fin (opcional): Índice donde termina el corte (no incluido). Si se omite, va hasta el final.

* paso (opcional): Salto entre elementos. Si es negativo, recorre la lista en orden inverso.

## 🔍 Ejemplo Práctico

```python
    # Definimos una lista de ejemplo
    numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Extraer una sublista (índices 2 a 5, 5 no incluido)
    sub1 = numeros[2:5]  
    print("Sublista [2:5]:", sub1)  # [30, 40, 50]

    # Desde el inicio hasta el índice 4 (no incluido)
    sub2 = numeros[:4]  
    print("Sublista [:4]:", sub2)  # [10, 20, 30, 40]

    # Desde el índice 5 hasta el final
    sub3 = numeros[5:]  
    print("Sublista [5:]:", sub3)  # [60, 70, 80, 90]

    # Paso de 2 en 2 (todos los elementos pares)
    sub4 = numeros[::2]  
    print("Sublista [::2]:", sub4)  # [10, 30, 50, 70, 90]

    # Invertir la lista
    sub5 = numeros[::-1]  
    print("Sublista invertida [::-1]:", sub5)  # [90, 80, 70, 60, 50, 40, 30, 20, 10]

    # Modificar una sublista (reemplazar elementos 3 a 6)
    numeros[3:6] = [100, 200, 300]  
    print("Lista modificada:", numeros)  # [10, 20, 30, 100, 200, 300, 70, 80, 90]

    # Eliminar elementos (del índice 1 al 3)
    numeros[1:4] = []  
    print("Lista después de eliminar:", numeros)  # [10, 200, 300, 70, 80, 90]
```

## Objetivo del desafío

El objetivo es imprimir diferentes posiciones de la lista, reemplazar un elemento e imprimir la lista con los nuevos resultados.

## Conceptos Aprendidos
* Slicing de listas con diferentes parámetros

* Reemplazo de elementos usando slicing

* Comportamiento de los índices positivos y negativos

* Modificación in-place de listas

## Cómo Usar
* Clona este repositorio

* Ejecuta el script Python: 

```bash
    python [nombre-desafio].py
```

* Observa los resultados y experimenta modificando los valores

### Contribuciones

Las sugerencias y mejoras son bienvenidas. Abre un issue o envía un pull request.

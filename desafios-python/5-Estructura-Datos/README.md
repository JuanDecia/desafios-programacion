# 📊 Estructuras de Datos en Python

Este directorio contiene ejercicios y ejemplos prácticos para dominar las estructuras de datos fundamentales en Python:

## 🎯 Objetivos de Aprendizaje

* Diferenciar estructuras mutables vs inmutables

* Dominar operaciones básicas en cada estructura

* Aplicar estructuras anidadas

* Implementar algoritmos eficientes

## 🧱 Estructuras Cubiertas

### 1. Listas

```python
    mi_lista = [1, "Python", True]
```

* Mutables: Se pueden modificar después de su creación

* Uso común: Almacenar colecciones de items ordenados

### 2. Tuplas

```python
    mi_tupla = (1, "Python", False)
```

* Inmutables: No se pueden modificar después de su creación

* Uso común: Datos que no deben cambiar (coordenadas, configuraciones)

### 3. Diccionarios

```python
    mi_dict = {"clave": "valor", "BTC": "Bitcoin"}
```

* Pares clave-valor: Acceso rápido mediante claves únicas

* Uso común: Representar objetos complejos (ej: datos API)

### 4. Conjuntos

```python
    mi_set = {1, 2, 3, 3}  # Resultado: {1, 2, 3}
```

* No duplicados: Elimina automáticamente elementos repetidos

* Uso común: Operaciones matemáticas (uniones, intersecciones)

## 📂 Estructura del Directorio

```bash
    /5-estructuras-datos/
    ├── 1-listas/
    │   ├── operaciones_basicas.py
    │   └── list_comprehensions.py
    ├── 2-tuplas/
    │   └── unpacking.py
    ├── 3-diccionarios/
    │   ├── dict_fromkeys.py
    │   └── nested_dicts.py
    ├── 4-conjuntos/
    │   └── operaciones_conjuntos.py
    └── README.md
```

## 🔍 Navegación 

* Clona el repositorio (ejemplo clonacion) 

* Navegá hasta un desafío especifico y clonalo (ejemplo) 

* Ejecuta el script (ejemplo) 

## 💡 Ejercicios Prácticos Recomendados

### Para Listas:

* Implementar una pila (stack) usando listas

* Filtrar elementos con list comprehensions

### Para Diccionarios:

* Crear un traductor simple (palabra → significado)

* Procesar datos JSON de APIs

### Para Conjuntos:

* Encontrar elementos comunes entre dos listas

* Eliminar duplicados de una lista

## 📌 Contribuciones 

* Abre un issue 

* Haz un fork y envía un pull request  
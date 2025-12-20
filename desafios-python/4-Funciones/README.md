# 📂 Directorio 4 - Funciones en Python

Este directorio contiene ejercicios y ejemplos prácticos para dominar el uso de funciones en Python.

## 🎯 Objetivos de aprendizaje

* Organizar código en bloques lógicos
* Reutilizar lógica sin repetir código
* Facilitar el mantenimiento y depuración
* Mejorar la legibilidad del programa

## 🚀 Conceptos Cubiertos

1. Definición, Sintaxis y Funcionamiento
2. Parámetros en funciones
3. Retornos en funciones
4. Niveles de las funciones
5. Tipo de funciones

## 🧠 Definición y Conceptos

Una función en Python es un bloque de código reutilizable que:

* Realiza una tarea específica
* Puede recibir datos de entrada (parámetros)
* Puede devolver resultados (return)
* Se define con la palabra clave def

Dentro de los conceptos principales, se desatacan las siguientes características:

* Modularización: Dividir programas complejos en partes más pequeñas
* Reutilización: Evitar repetir el mismo código múltiples veces
* Abstracción: Ocultar detalles de implementación
* Organización: Mejorar legibilidad y mantenimiento del código

## ⚙️ Sintaxis y Funcionamiento

```python
    def nombre_funcion(parámetros):
        """Docstring (documentación)"""
        # Cuerpo de la función
        return valor  # Opcional
```

## 📁 Estructura y Navegación de Directorio

```bash
└── /funciones/
|	├── README.md
|	├── /directorio-desafios/
|   |   ├── solucion-desafio.py
|   |   └── README.md
    └── ...
```

## 🚀 Cómo usar el repositorio

1.	Clona el repositorio 
2.	Navega hasta un desafío especifico y clonalo
3.	Ejecuta el script

## 📝 Operaciones Básicas - Variaciones de Funciones

### Funcióin sin parámetros

```python
    def saludar():
        print("¡Hola, bienvenido!")

    saludar()  # Output: ¡Hola, bienvenido!
```

### Función con valor por defecto

```python
    def potencia(base, exponente=2):
        return base ** exponente

    print(potencia(3))    # 9 (usa exponente=2 por defecto)
    print(potencia(3, 3)) # 27
```

## 📚 Niveles de funciones

* Básico: Funciones simples sin parámetros

* Intermedio: Funciones con retorno y parámetros

* Avanzado: Funciones anidadas y decoradores

## ✅ Tipos de Funciones

* Built-in: print(), len(), etc.
* Definidas por usuario: Las que tú creas
* Lambda: Funciones anónimas de una línea

## 📌 Contribuciones
*	Abre un issue
*	Haz un fork y envía un pull request
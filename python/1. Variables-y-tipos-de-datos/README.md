# 📂 1. Variables y Tipos de Datos en Python

Este directorio contiene ejercicios y ejemplos fundamentales sobre el manejo de variables y los tipos de datos básicos en Python, esenciales para construir una base sólida en programación.

## 🎯 Objetivos de Aprendizaje

* Comprender qué son las variables y cómo declararlas
* Dominar los tipos de datos primitivos en Python
* Aprender las reglas de nomenclatura para variables
* Practicar la conversión entre tipos de datos (type casting)
* Identificar casos de uso para cada tipo de dato

## 🚀 Conceptos Cubiertos

**1. Variables (Declaración y Asignación)**

```python
    nombre = "Ana"       # str 
    edad = 25            # int 
    altura = 1.65        # float 
    es_estudiante = True # bool
```

**2. Tipos de Datos Básicos**

| Tipo | Ejemplo | Características |
|------|---------|-----------------|
| int |	42 | Números enteros |
| float | 3.14 | Números decimales |
| str |	"Hola Python" |	Cadena de caracteres |
| bool | True/False | Valores booleanos |
| None | None |	Representa ausencia de valor |

**3. Operaciones Básicas**

```python

# Concatenación
nombre_completo = nombre + " Pérez"  

# Operaciones matemáticas
suma = edad + 5  

# Conversión de tipos
edad_str = str(edad)  
```

## 📁 Estructura del Directorio

```text
/1-variables-tipos-datos/
  ├── /subtema-1/  
  │   ├── README.md    # Explicación detallada
  │   ├── /desafio-1/      # Validación de tipos
  │   |     ├── README.md    # Enunciado del problema
  │   |     ├── solucion.py  
  │   |     └── tests/       # Pruebas automáticas
  │
  ├── /subtema-2/  
  │   ├── README.md    # Explicación detallada
  │   ├── /desafio-1/      # Validación de tipos
  │   |     ├── README.md    # Enunciado del problema
  │   |     ├── solucion.py  
  │   |     └── tests/       # Pruebas automáticas
  └── ...
```

## 🔍 Navegación

**1. Clona el repositorio:**

```bash
    git clone https://github.com/[tu-usuario]/python-basico.git
```

**2. Accede a esta sección:**

```bash
    cd python-basico/1-variables-tipos-datos
```

**3. Ejecuta cualquier ejemplo:**

```bash
    python ejemplo-1/ejemplo.py
```

## 📌 Contribuciones

¡Aportes bienvenidos! Sigue estos pasos:

Reporta errores: Abre un issue con el tag bug

Mejora ejemplos: Envía un pull request con tus mejoras

Propone nuevos ejercicios: Usa la plantilla de issue

```bash
    # Pasos para contribuir:
    1. Haz fork del repositorio
    2. Crea una rama (git checkout -b mejora-variables)
    3. Realiza tus cambios y haz commit
    4. Envía el PR con una descripción clara
```
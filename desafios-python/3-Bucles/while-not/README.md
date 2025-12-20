# Bucle While Not

## 🧠 Definición y Concepto

El bucle **while not** es una variante del bucle while tradicional que se ejecuta mientras una condición **NO** sea verdadera. Es particularmente útil cuando queremos:

* Esperar hasta que un estado cambie

* Verificar que algo deja de ser falso

* Mantener un bucle hasta que se cumpla una condición negativa

## ⚙️ Sintaxis y Funcionamiento

### Sintaxis

```python
    while not condición:
        # Bloque de código que se ejecuta
        # mientras la condición sea FALSA
```

### Funcionamiento

1. Evalúa si la condición es False (por el not)

2. Si es False, ejecuta el bloque de código

3. Vuelve a evaluar la condición

4. Sale del bucle cuando la condición se hace True

## 📝 Ejemplo Práctico

```python
# Ejemplo: Esperar hasta que el usuario ingrese "salir"
comando = ""
    while not comando == "salir":
        comando = input("Ingrese un comando ('salir' para terminar): ")
        print(f"Ejecutando: {comando}")
        print("Programa terminado")
```

### ⚠️ Consideraciones Importantes

* Condición de salida: Asegúrate que la condición eventualmente se haga True para evitar bucles infinitos

* Legibilidad: A veces es más claro usar while not que su equivalente con while y operadores lógicos

* Alternativas: Puedes lograr lo mismo con while condición == False pero while not es más idiomático en Python

## 📁 Estructura de Directorio

```text
└── /Subtema/
	├── README.md
	├── [directorio-desafio]/
           ├── solucion-desafio.py
           └── README.md
```

## 🏆 Desafíos Propuestos
*(Este listado se actualizará conforme se añadan ejercicios)*

1. Validación número: Programa para ejecutar una validación de un número utilizando el bucle **while not**

2. Validación Criptos: este desafío demuestra cómo validar que un valor ingresado por el usuario esté presente en un array predefinido de criptomonedas, utilizando un bucle while para garantizar la entrada correcta.


## 📌 Contribuciones y Mejoras
•	Abre un issue
•	Haz un fork y envía un pull request
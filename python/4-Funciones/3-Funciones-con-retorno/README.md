# 🚀 Funciones con Retorno

Una función con retorno es una función que devuelve uno o más valores al finalizar su ejecución utilizando la palabra clave **return**. Estos valores pueden ser almacenados en variables, utilizados en expresiones o pasados a otras funciones.

## 🔧 Sintaxis y funcionamiento

```python
    def nombre_funcion(parametros):
        # Código de la función
        return valor  # Devuelve el resultado
```

* Termina la ejecución de la función inmediatamente.

* Puede devolver cualquier tipo de dato (int, float, string, lista, tupla, diccionario, etc.).

* Puede devolver múltiples valores (en forma de tupla).

## 📌 Tipos de retorno

### Retorno Simple

```python
    def calcular_iva(monto):
        iva = monto * 0.21
        return iva  # Retorna un solo valor

    total_iva = calcular_iva(1000)  # total_iva = 210.0
```

### Retorno múltiple

```python
    def operaciones_basicas(a, b):
        suma = a + b
        resta = a - b
        return suma, resta  # Retorna tupla

    s, r = operaciones_basicas(10, 5)
    print(f"Suma: {s}, Resta: {r}")  # Suma: 15, Resta: 5
```

### Retorno Condicional

```python
    def es_mayor_de_edad(edad):
        if edad >= 18:
            return True
        else:
            return False

    puede_votar = es_mayor_de_edad(20)  # True
```

## 📁 Estructura del directorio

```bash
    └── /Directorio-Subtema/
	|   ├── README.md
	|   ├── /directorio-desafio/
    |   |   ├── solucion-desafio.py
    |   |   └── README.md
    └── ...
```

## ✅ Desafíos Realizados

* Calculadora Crecimiento de Criptomonedas: Programa para calcular el crecimiento estimativo de una criptomoneda.

## 📌 Contribuí

* Abre un issue
* Haz un fork y envía un pull request

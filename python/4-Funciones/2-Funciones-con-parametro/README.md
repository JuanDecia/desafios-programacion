# 🔠 Parámetros en la función

Los parámetros son variables especiales que reciben datos cuando llamamos a una función. Actúan como "espacios reservados" para los valores reales (argumentos) que pasaremos al invocar la función.

## ⚙️ Sintaxis y Funcionamiento

### Parámetros posicionales

Los más comunes, se asignan por orden:

```python
    def calcular_area_rectangulo(base, altura):
        return base * altura

    print(calcular_area_rectangulo(5, 3))  # 15 (5→base, 3→altura)
```

### Parámetros con valores por defecto

Tienen un valor preestablecido si no se proporciona:

```python
    def saludar(nombre, mensaje="Hola"):
        return f"{mensaje}, {nombre}!"

    print(saludar("Ana"))            # "Hola, Ana!"
    print(saludar("Carlos", "Hey"))  # "Hey, Carlos!"
```

### Parámetros arbitrarios

Reciben múltiples argumentos como tupla:

```python
    def sumar_numeros(*args):
        return sum(args)

    print(sumar_numeros(1, 2, 3))  # 6
    print(sumar_numeros(5, 10))     # 15
```

### Parámetros con nombres Kwargs

Reciben múltiples argumentos como diccionario

```python
    def mostrar_info(**kwargs):
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")

    mostrar_info(nombre="Luisa", edad=25, ciudad="Madrid")
    # nombre: Luisa
    # edad: 25
    # ciudad: Madrid
```

### Combinación de tipos de parámetros

Orden correcto en la definición:

1. Parámetros posicionales

2. *args

3. Parámetros con valor por defecto

4. **kwargs

```python
    def funcion_completa(a, b, *args, c=10, **kwargs):
        print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

    funcion_completa(1, 2, 3, 4, c=5, x=7, y=9)
    # a: 1, b: 2, args: (3, 4), c: 5, kwargs: {'x': 7, 'y': 9}
```

### Función con parámetros simple

```python
    def sumar_dos_numeros(a, b):
    """
    Suma dos números y devuelve el resultado
    
    Parámetros:
        a (int/float): Primer número
        b (int/float): Segundo número
    
    Retorna:
        int/float: Resultado de la suma
    """
    resultado = a + b
    return resultado

    # Llamando a la función
    total = sumar_dos_numeros(5, 3)
    print(f"La suma es: {total}")  # Output: La suma es: 8
```

### Desgloce de Ejemplo

1. Declaración:

* **def**: Palabra clave para definir funciones

* **sumar_dos_numeros**: Nombre descriptivo (usa snake_case)

* **(a, b)**: Parámetros de entrada

2. Docstring:

* """Explica qué hace la función (Documentación entre triple comillas)"""

* Describe parámetros y valor de retorno

3. Cuerpo:

* Operación matemática básica (a + b)

* Asignación a variable resultado

4. Retorno:

* **return** resultado: Devuelve el cálculo

5. Llamada:

```python
    sumar_dos_numeros(5, 3)  # Argumentos posicionales
```

## 📁 Estructura del directorio

```text
└── /funciones-con-parametros/
	├── README.md
	├── /nombre-desafio/
           ├── solucion-desafio.py
           └── README.md
```

## 🏆 Desafíos Propuestos

## ✅ Desafíos Realizados

1. Convertir Montos: Función para convertir montos de criptomonedas

## 📌 Contribuciones

*	Abre un issue
*	Haz un fork y envía un pull request

# 📊 Desafío #1: Conversión de Criptomonedas a USD

Este desafío consiste en crear una función (Función conversionCriptomoneda()) que calcule el valor total en dólares estadounidenses (USD) de una cantidad acumulada de dos criptomonedas, utilizando tasas de conversión desde una api.

## 🎯 Enunciado y Requisitos

1. Crear una función llamada conversionCriptomoneda que reciba dos criptomonedas.

2. La función debe calcular el valor total en USD basado en tasas de conversión a través de la API.

3. Solicitar ingreso del nombre de la criptomoneda y la cantidad

4. Validar las entradas de datos para un sistema robusto.

5. Mostrar el resultado formateado en un mensaje legible.

**Requisitos obligatorios**
* La función debe llamarse conversionCriptomoneda.
* Validar entrada de números y nombres de las cripto.
* Debe retornar el valor total en USD.
* El resultado debe imprimirse en consola con un mensaje claro.

## 🔧 Requisitos Técnicos

* Python 3.8+ (Recomendado 3.10+)

* Instalar e importar librería requests

* Editor de código (VS Code, PyCharm, Jupyter Notebook, etc.)

## 🌐 Cómo Usar

1. Clona el repositorio:

```bash
    git clone https://github.com/tu-usuario/cripto-conversor.git
    cd cripto-conversor
```

2. Ejecuta el script (guardado como cripto_conversor.py):

```bash
    python cripto_conversor.py
```

3. Modifica los valores para probar diferentes cantidades:

```python
    conversionCriptomoneda(10, 5000)  # Ejemplo adicional
```

## ✅ Ejemplo de Entrada/Salida

**Entrada**:

```bash
    Ingrese la cantidad de BTC: 1
    Ingrese la cantidad de XRP: 1
```

**Salida**:

```text
    BTC ingresados: 1
    XRP ingresados: 1
    La suma de la cantidad de sus monedas es de USD$: 50.66
```

## 📚 Conceptos Aprendidos
* Declaración de funciones con def.
* Parámetros posicionales en funciones.
* Operaciones aritméticas básicas (+, *).
* Conversión de tipos (str() para concatenación).
* Formateo de salida en consola.

## 📌 Novedades, Mejoras Clave, Actualizaciones

* Versión 1.0 (Actual):
* Conversión básica de BTC y XRP a USD.
* Tasas de cambio fijas integradas en la función.
* Posibles actualizaciones:

1. Añadir más criptomonedas (ETH, SOL, etc.).
2. Usar APIs para tasas en tiempo real (ejemplo: CoinGecko).

## 🔥 Últimas mejoras aplicadas

✅ Función **main()** que controla el programa  
✅ Formato de impresión para combinar valores y texto
✅ Funcion para convertir monedas y solicitar datos al usuario
✅ Se validan los datos que ingresa el usuario
✅ La funcion retorna 2 decimales
✅ Validación de nombre de criptomonedas
✅ Importar valores reales de criptomonedas

## 📌 Contribuir

¡Contribuciones son bienvenidas! Sigue estos pasos:

Reporta errores: Abre un issue en GitHub.

Propone mejoras: Haz un fork y envía un pull request.

Sugiere nuevas features: ¿Conversión inversa? ¿Más criptos?

```bash
    # Flujo típico para contribuir:
    1. fork repositorio
    2. git clone tu-fork-url
    3. git checkout -b nueva-feature
    4. Haz tus cambios + commits
    5. git push origin nueva-feature
    6. Abre Pull Request
```
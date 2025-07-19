# 📊 Ordenador de Criptomonedas por Cantidad

Programa que recibe tres criptomonedas con sus cantidades y las muestra ordenadas de mayor a menor.

## 🔍 Enunciado
El programa debe:
1. Solicitar al usuario los nombres y cantidades de 3 criptomonedas.
2. Mostrarlas ordenadas de forma decreciente según su cantidad.
3. Manejar posibles empates (aunque el código actual los muestra en orden de entrada).

## 📋 Requisitos
- Usar estructuras condicionales anidadas (`if-elif-else`).
- Validar que las cantidades sean numéricas.
- Mostrar el resultado formateado claramente.

## 🎯 Ejemplo de Entrada/Salida

```python
    # Ejemplo 1:
    Ingrese el nombre de la primera moneda: BTC
    Ingresa la cantidad de BTC: 1.5
    Ingrese el nombre de la segunda moneda: ETH
    Ingresa la cantidad de ETH: 3.2
    Ingrese el nombre de la tercera moneda: SOL
    Ingresa la cantidad de SOL: 5.1

    SOL 5.1
    ETH 3.2
    BTC 1.5

    # Ejemplo 2 (con empate):
    Ingrese el nombre de la primera moneda: ADA
    Ingresa la cantidad de ADA: 10
    Ingrese el nombre de la segunda moneda: DOT
    Ingresa la cantidad de DOT: 10
    Ingrese el nombre de la tercera moneda: XRP
    Ingresa la cantidad de XRP: 8

    ADA 10
    DOT 10
    XRP 8

```

## 🚀 Cómo Ejecutar

* Navega al directorio:

```bash
    cd python/2-condicionales/ordenar-criptomonedas
```

* Ejecuta:

```bash
    python solucion.py
```

## 🛠️ Mejoras Posibles

* Usar listas y el método sort() para simplificar la lógica.

* Añadir validación de entradas numéricas.

* Mostrar el valor en USD junto al ordenamiento.

---
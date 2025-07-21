# 💰 Conversor de Criptomonedas a USD

Desafío práctico para aplicar condicionales simples, convirtiendo cantidades de criptomonedas (BTC, DASH, LTC) a dólares estadounidenses (USD).

## 🔍 Enunciado
El programa debe:
1. Pedir al usuario que ingrese una moneda (BTC, DASH o LTC).
2. Validar que la moneda sea soportada.
3. Si es válida, solicitar una cantidad y convertirla a USD según el valor de la moneda.
4. Mostrar el resultado o un mensaje de error.

## 📋 Requisitos
- Usar estructuras condicionales (`if-elif-else`).
- Validar entrada del usuario.
- Manejar números decimales.

## 🎯 Ejemplo de Entrada/Salida

```python
    # Ejemplo 1:
    Ingrese la moneda a utilizar(BTC, DASH o LTC): BTC
    Ingrese la cantidad a utilizar: 0.5
    La cantidad de USD recargado fue de: 3815.4
    
    # Ejemplo 2:
    Ingrese la moneda a utilizar(BTC, DASH o LTC): ETH
    Error: Solo se permite utilizar BTC, DASH o LTC
```

## 🚀 Cómo Ejecutar

* Navega al directorio del desafío:

```bash
cd python/2-condicionales/conversor-cripto

* Ejecuta el script:
    python solucion.py
```

## 📌 Mejoras a aplicar

* Caché de precios: guardar los precios en un JSON para no depender de la API.
* Añadir más criptos.
* Guardar historial de consultas.

---

# 📊 Registro de Criptomonedas con Arreglos

## 📝 Descripción
El programa debe permitir registrar 5 criptomonedas con sus cantidades y precios en USD, utilizando arreglos para almacenar y mostrar los datos.

- **Validación de monedas**: Solo acepta BTC, BCC, LTC, ETH, ETC
- **Validación numérica**: Asegura que cantidades y precios sean valores numéricos
- **Almacenamiento en arreglos**: Usa listas separadas para nombres, cantidades y cotizaciones
- **Visualización estructurada**: Muestra los datos en formato claro

## 🎯 Objetivos de Aprendizaje

* Manejo de arreglos (listas) en Python

* Validación de inputs del usuario

* Uso de bucles while para control de flujo

* Formateo de strings para salida estructurada

## 📊 Ejemplo de Ejecución

```bash
    Ingrese el nombre de la moneda: btc
    Ingrese la cantidad de btc: 1.5
    Ingrese la cotización en USD de btc: 50000

    ... (repetido para 5 monedas)...

    Resumen de criptomonedas:
    Moneda: btc, Cantidad: 1.5, Valor en USD: 50000
    Moneda: eth, Cantidad: 10, Valor en USD: 3000
    ...
```

## 💡 Mejoras Sugeridas

* Usar diccionarios en lugar de múltiples arreglos:

```python

    registros = [
        {'moneda': 'btc', 'cantidad': 1.5, 'cotizacion': 50000},
        ...
    ]
```

* Añadir cálculos automáticos:

```python
    valor_total = float(cant[i]) * float(cotiz[i])
```

* Implementar funciones para cada operación:

```python
    def ingresar_moneda():
        # Lógica de ingreso
        return moneda, cantidad, cotizacion
```

## 🚀 Cómo Ejecutar

* Guardar como cripto_arrays.py

* Ejecutar en terminal:

```bash
    python cripto_arrays.py
```
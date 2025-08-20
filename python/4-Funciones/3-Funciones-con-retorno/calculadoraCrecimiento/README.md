# Calculadora de Crecimiento de Criptomonedas 🚀💰

Este programa en Python calcula el valor actual de una criptomoneda en USD y proyecta su crecimiento semanal con un rendimiento del 5% diario. Además, muestra la fecha y hora exacta de la consulta.

## 📄 Enunciado:

* Cálculo en tiempo real: Valor actual de la criptomoneda en USD.

* Fecha y hora de la consulta (time.strftime).

* Proyección de ganancias: Simula un crecimiento del 5% diario durante 5 días (semana laboral).

* Formatea el resultado a 2 decimales para claridad.

## 🔧 Requisitos Técnicos

* Python 3.8+
* Librería Requests (instalación e importación)
* IDE

## 🌐 Cómo Usarlo

1. Clona el repositorio

2. Ejecutar el script

```bash
    python calculadora_cripto.py
```

3. Modifica las variables:

nombre_cripto: Nombre de la criptomoneda.

cantidad_cripto: Cantidad acumulada.

cotizacion: Precio actual en USD.

## ✅ Salida esperada:

Fecha: Wed Jun 26 12:30:45 2024 | Saldo actual: $4001.00 en Bitcoin
Proyección en 5 días (+5% diario): $5105.13

## 📚 Conceptos aprendidos

* Manipulación de Fechas y Horas: time.strftime("%c") - Formatea la fecha/hora actual en un string legible.

* Operaciones Matemáticas Financieras

    - Cálculo del crecimiento del 5% diario (valor * (1.05 ** días)).

    - Fórmulas para proyecciones financieras y crecimiento exponencial.

* Formateo de números: "{0:.2f}".format() para limitar a 2 decimales.

* Estructuras Básicas de Python

    - Variables y tipos de datos:

    - Uso de float para cantidades y cotizaciones.

    - Print formateado:

    - Concatenación con + y f-strings (f"Texto {variable}").

* Extensiones (Conceptos Avanzados)

* APIs en tiempo real: Conexión a CoinGecko/Binance para obtener precios actuales (usando requests).

* Validación de entradas: Evitar errores si el usuario ingresa texto en vez de números (try-except).

* Funciones modulares: Separar lógica en funciones como calcular_ganancia() o obtener_cotizacion().

* Buenas prácticas: Legibilidad del código y documentación (como este README).

## 📌 Posibles Mejoras

Interfaz gráfica con tkinter o streamlit.

## 📄 Licencia

MIT License. ¡Usa, modifica y comparte libremente!
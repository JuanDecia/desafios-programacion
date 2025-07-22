# 🏦 Billetera de Criptomonedas

Aplicación para gestionar un portafolio de criptomonedas con:
- Registro de transacciones
- Balance en tiempo real
- Persistencia de datos
- Precios actualizados vía API

## 🚀 Cómo Usar
1. Ejecutar el script:
    ```bash
        python billeteraCrypto.py
    ```

* Seguir el menú interactivo

## 🔧 Requisitos

* Python 3.8+

* Librerías: pycoingecko

* API CoinGecko (conexión a internet)

## 📌 Estructura de Datos

* Los datos se guardan en cuenta_cripto.json con:

```json
    {
        "saldos": {"BTC": 0.5, "LTC": 10.0},
        "transacciones": [
            {
                "fecha": "2023-11-15T12:30:00",
                "moneda": "BTC",
                "cantidad": 0.5,
                "precio_usd": 50000.0
            }
        ]
    }
```

## 📌 Novedades y Mejoras Clave

- Estructura Profesional:

* Clase BilleteraCripto autocontenida

* Persistencia en JSON automática

* Manejo robusto de errores

- Funcionalidades Extendidas:

* Sistema de menú interactivo

* Registro con timestamps

* Balance ordenado por valor USD

* Historial detallado de transacciones

- Documentación:

* Docstrings explicativas

* Tipado de datos claro

- Seguridad:

* Validación de entradas

* Fallback a valores por defecto

## 💡 Mejoras Futuras

* Gráficos de evolución

* Soporte para más criptomonedas

* Exportar a CSV/Excel

---
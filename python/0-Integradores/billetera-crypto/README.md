# 🏦 Billetera de Criptomonedas

## 🎯 Objetivo

Crear una aplicación para gestionar una billetera virtual de criptomonedas con las siguientes características:

- Registro de transacciones
- Balance en tiempo real
- Persistencia de datos
- Precios actualizados vía API

## 🔧 Requisitos

* Python 3.8+

* Librerías: pycoingecko

* API CoinGecko (conexión a internet)

## 🚀 Cómo Usar

1. Clona el repositorio

```bash
    git clone https://github.com/JuanDecia/desafios-programacion/tree/main/python/0.%20Integradores/billetera-crypto
```

2. Ejecutar el script

```bash
    python billeteraCrypto.py
```

* Seguir el menú interactivo
* Observa los resultados y experimenta modificando los valores

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

### 📌 Contribuir
•	Abre un issue
•	Haz un fork y envía un pull request 

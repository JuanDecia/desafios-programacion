# 🔍 Validador de Criptomonedas con CoinMarketCap API

## 📝 Descripción

Programa que verifica si una criptomoneda existe en CoinMarketCap mostrando su nombre completo y símbolo (ej: BTC → Bitcoin).

Posteriormente, el programa debe imprimir el nombre abreviado. Para esto se debe utilizar el módulo requests, 
usando la API, que nos retornará un json() con la lista de las cripto. Entre estos esta el nombre completo 
de las monedas y el nombre abreviado. Hacer uso de variables diccionarios y tuplas.

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Módulo `requests`
- API CoinMarketCap (Professional)

## ⚙️ Configuración Necesaria

1. Obtener API Key gratuita en [CoinMarketCap Pro](https://pro.coinmarketcap.com/)

2. Reemplazar en el código:

```python
   COINMARKET_API_KEY = "tu_api_key_aquí"
```

# Configuración API

```python
    API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    API_KEY = "tu_api_key_aquí"
    HEADERS = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }

    # Obtener datos
    try:
        respuesta = requests.get(API_URL, headers=HEADERS)
        datos = respuesta.json()
        monedas = {
            cripto["symbol"]: cripto["name"]
            for cripto in datos["data"]
        }
    except Exception as e:
        print(f"⚠️ Error al conectar con la API: {e}")
        monedas = {}  # Diccionario vacío como fallback
```

# Interacción con usuario

```python
    while True:
        simbolo = input("Ingrese el símbolo de la cripto (ej: BTC): ").strip().upper()
        
        if not simbolo:
            print("❌ El símbolo no puede estar vacío")
            continue
            
        if es_moneda_valida(simbolo):
            print(f"✅ {simbolo} = {monedas[simbolo]} (válido)")
            break
        else:
            print(f"❌ Símbolo no encontrado. Intente con: {', '.join(monedas.keys()[:3])}...")
```

## 📊 Ejemplo de Uso

```bash
    $ python validador_cripto.py
```

* Consola

```bash
    Ingrese el símbolo de la cripto (ej: BTC): eth
    ✅ ETH = Ethereum (válido)
```

## 🧠 Conceptos Clave

* Diccionarios: Almacenan pares símbolo:nombre

* API REST: Consumo de datos en formato JSON

* Manejo de errores: Validación de entrada y conexión

## 🚀 Cómo Ejecutar

* Instalar dependencias:

```bash
    pip install requests
    Guardar como validador_cripto.py
```

* Ejecutar:

```bash
    python validador_cripto.py
```

## 💡 Mejoras Futuras

* Cachear resultados para evitar llamadas repetidas

* Añadir búsqueda por nombre (no solo símbolo)

* Mostrar precio actual y cambio porcentual

⚠️ Nota: El plan gratuito de CoinMarketCap tiene límite de 10,000 llamadas/mes
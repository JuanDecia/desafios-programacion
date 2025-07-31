## Librerías necesarias
import requests
import sys

# Obtiene los datos de las cripto y almacena en un diccionario
def obtener_datos_cripto(api_key: str) -> dict:

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
    }

    try:

        # Petición a la API de CoinMarketCap (obtiene lista de cripto)
        response = requests.get(url, headers = headers)
        response.raise_for_status() # Lanza un error si la petición falla
        datos = response.json()
        
        return {
            # Crea un diccionario con el símbolo y nombre de las cripto
            cripto["symbol"]: cripto["name"]
            for cripto in datos["data"]
        }
    
    except Exception as e:
        print(f"Error al obtener datos: {e}", file=sys.stderr)
        return None

## Valida si la criptomoneda
def validar_moneda(monedas: dict) -> str:
    
    while True:

        symbol = input("Indique el nombre de la moneda a verificar: ").strip().upper()

        if not symbol:
            print("❌ El símbolo no puede estar vacío")
            continue

        if symbol in monedas:
            return symbol
        
        print(f"❌ Símbolo inválido. Opciones válidas: {', '.join(monedas.keys())}")

# Funcion Principal
def main():

    print("\n=== VALIDADOR DE CRIPTOMONEDAS ===")

    # API_KEY
    COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"

    # Debug: Verificar conexión
    monedas = obtener_datos_cripto(COINMARKET_API_KEY)

    if not monedas:
        print("❌ Fallo al obtener datos. Posibles causas:")
        print("- API Key inválida o sin créditos")
        print("- Problemas de conexión a Internet")
        print("- Cambios en la estructura de la API")
        sys.exit(1)
    
    # Debug: Mostrar las primeras 5 monedas
    print("\nMonedas disponibles (ejemplos):")
    for simbolo in list(monedas.keys())[:5]:
        print(f"{simbolo}: {monedas[simbolo]}")
    
    # Validación
    simbolo = validar_moneda(monedas)
    print(f"\n✅ {simbolo} = {monedas[simbolo]} (válido)\n")

# Ejecuta la funcion principal
if __name__ == "__main__":
    main()
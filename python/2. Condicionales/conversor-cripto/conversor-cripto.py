### CONDICIONALES DESAFÍO 1

# Librerías necesarias
from pycoingecko import CoinGeckoAPI

# Inicializa la API de CoinGecko
cg = CoinGeckoAPI()

# obtener precios de BTC, DASH y LTC
def obtener_precio():

    try:
        data = cg.get_price(ids='bitcoin,litecoin,dash', vs_currencies='usd')
        return {
            "BTC": data["bitcoin"]["usd"],
            "LTC": data["litecoin"]["usd"],
            "DASH": data["dash"]["usd"]
        }
    except Exception as e:
        print(f"Error al obtener el precio: {e}.")
        return None
    
# Convertir monedas a USD
def convertir_cripto():

    prices = obtener_precio()
    if not prices:
        return None
    
    moneda = input("Ingrese moneda solo (BTC, DASH o LTC): ").strip().upper()
    if moneda in prices:
        try:
            cantidad = float(input("Ingrese la cantidad a convertir: "))
            monto = cantidad * prices[moneda]
            print(f"\n💵 {cantidad} {moneda} = ${monto:,.2f} USD")
            print(f"ℹ️ Precio actual: 1 {moneda} = ${prices[moneda]:,.2f} USD \n")
        except ValueError:
            print("Error: La cantidad ingresada no es válida.")
    else:
        print("Error: Moneda no soportada. Solo se permite BTC, DASH o LTC.")


if __name__ == "__main__":
    print("Obteniendo precios actualizados...")
    convertir_cripto()


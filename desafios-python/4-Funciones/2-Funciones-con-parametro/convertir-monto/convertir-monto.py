import requests

# Recibir valores de la criptomoneda
def get_price(cripto: str) -> float:

    #1 Mapeo Criptos
    criptos = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "LTC": "litecoin"
    }

    #2 Convertir entrada a mayúsculas y validar
    cripto.upper()
    if cripto not in criptos:
        print(f"Criptomoneda {cripto} no soportada.")
        return None

    #3 Construcción url API
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={criptos[cripto]}&vs_currencies=usd"

    #4 Petición y manejo de errores
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        data = response.json()
        price = data[criptos[cripto]]['usd']

        return float(price)
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el precio de {cripto}: {e}")
        return None
    
# Convierte una cantidad de criptomoneda a usd
def conversion(cantidad: str, cripto: str) -> float:

    """
    Args:
        cripto: Símbolo de la criptomoneda (ej: 'BTC')
        cantidad: Cantidad a convertir (debe ser > 0)
    
    Returns:
        Valor en USD o None si hay error
    """

    # 1. Validar criptomoneda
    precio = get_price(cripto)
    if precio is None:
        print(f"Error: No se pudo obtener el precio de la {cripto}")
        return None

    # 2. Validad cantidad
    if cantidad <= 0:
        print("Error: la cantidad debe ser positiva")
        return None
    
    # 3. Calcular y retornar los valores
    total_usd = float(cantidad * precio)
    print(f"{cantidad} {cripto.upper()} son ${total_usd:.2f} USD")
    return total_usd

# Función ejecutadora del programa
def main():
    print("=== CONVERTIDOR DE MONEDAS ===")
    
    while True:  # Bucle principal
        # 1. Pedir cripto
        while True:
            cripto = input("\nIngrese cripto (BTC/ETH/LTC): ").upper()
            if cripto in ["BTC", "ETH", "LTC"]:
                break
            print("Cripto no válida")
        
        # 2. Pedir cantidad
        while True:
            try:
                cantidad = float(input("Ingrese cantidad: "))
                if cantidad > 0:
                    break
                print("Debe ser positivo")
            except ValueError:
                print("Ingrese un número válido")
        
        # 3. Convertir
        resultado = conversion(cantidad, cripto)
        
        # 4. Preguntar por otra conversión
        while True:
            continuar = input("\n¿Otra conversión? (s/n): ").lower()
            if continuar in ("s", "n"):
                break
            print("Ingrese 's' o 'n'")
        
        if continuar == "n":
            print("\n¡Gracias por usar el conversor!")
            break

if __name__ == "__main__":
    main()
# Solicitar datos al usuario
def solicitarDatos():

    # Verifica que BTC y XRP sean números
    while True:
        try:
            btc = float(input("Ingrese la cantidad de BTC: "))
            xrp = float(input("Ingrese la cantidad de XRP: "))
            break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

    return btc, xrp

# Convertir datos solicitados
def conversionCriptomoneda(cantBTC,cantXRP):
    
    TASAS = {
        "BTC": 50,
        "XRP": 0.660982
    }

    # Calcula el total de la cantidad con el valor de las tasas
    totalUSD = (cantBTC * TASAS["BTC"]) + (cantXRP * TASAS["XRP"])

    # Redondea a 2 decimales
    totalUSD = round(totalUSD, 2)

    return str(totalUSD)

# Función Ejecutadora
def main():

    #Paso 1: Datos del usuario
    btc, xrp = solicitarDatos()

    #Paso 2: Conversión de criptomonedas
    conversionCriptomoneda(btc, xrp)

    #Paso 3: Mostrar resultados
    print(f"BTC ingresados: {btc}")
    print(f"XRP ingresados: {xrp}")
    print(f"La suma de la cantidad de las monedas ingresadas es de USD$: {conversionCriptomoneda(btc, xrp)}")

if __name__ == "__main__":
    main()

# Validador Criptomoneda
def validar_criptomoneda():

    criptos_validas = ["BTC","BCC","LTC","ETH","ETC"]

    print("💰 Validador de Criptomonedas")
    print("=" * 40)
    print("Monedas aceptadas:", ", ".join(criptos_validas))
    print("=" * 40)

    nombre_cripto = input("Ingrese el nombre de la criptomoneda: ")
    nombre_cripto = nombre_cripto.strip().upper()

    while nombre_cripto not in criptos_validas:
        mensaje_error = f"\n🚫 ERROR: '{nombre_cripto}' no está en la lista."
        print(mensaje_error)
        print("Por favor, elija una de estas opciones:")
        print(", ".join(criptos_validas))

        # Reingreso con mensaje completo pero en múltiples líneas
        nombre_cripto = input(
            "\nIngrese el nombre de la criptomoneda: "
        )
        nombre_cripto = nombre_cripto.strip().upper()

    return nombre_cripto

# Función Inicializadora
def main():

    cripto_valida = validar_criptomoneda()
    print(f"\n🎉 Moneda válida: {cripto_valida}")

if __name__ == "__main__":
    main()

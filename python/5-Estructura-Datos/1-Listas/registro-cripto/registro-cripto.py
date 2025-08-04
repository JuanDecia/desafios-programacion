## DESAFÍO LISTAS #1 ##

# Recibir Cripto
def getCripto(nombreCripto: str) -> bool:
    criptos = ["btc","bcc","ltc","eth","etc"]
    if nombreCripto in criptos:
        return True
    else:
        return False

# Verifica si el valor es un número
def isNumber(numero: str) -> bool:
    return numero.replace('.','',1).isdigit()

# Calcular valores totales
def calcularTotal(cantidades: list, valores: list) -> float:
    return sum([float(cantidad) * float(valor) for cantidad, valor in zip(cantidades, valores)])

# Mostrar resumen
def mostrarResumen(criptos: list, cantidades: list, valores: list):

    # Calcular total
    total = calcularTotal(cantidades, valores)

    print("\n" + "=" * 50)
    print(" Resumen de la billetera" .center(50, "="))
    print("=" * 50)

    for i, (cripto, cantidad, valor) in enumerate(zip(criptos, cantidades, valores), 1):

        subtotal = cantidad * valor
        print(f"\n{i}. {cripto.upper()}:")
        print(f"   Cantidad: {cantidad:.8f}")  # 8 decimales para cripto
        print(f"   Valor unitario (USD): ${valor:.2f}")
        print(f"   Subtotal: ${subtotal:.2f}")
    
    print("\n" + "-"*50)
    print(f"TOTAL DE LA BILLETERA: ${total:.2f}".rjust(50))
    print("="*50 + "\n")

def cargarMonedas():

    # Inicializar listas donde se guardarán los datos cargados
    criptos = []
    cantidades = []
    valores = []

    # Pedir al usuarios cantidad de monedas a registrar
    num_monedas = ""
    while True:
        try:
            num_monedas = int(input("¿Cuántas criptomonedas desea registrar? (min: 1 - max: 5): "))
            if num_monedas > 0:
                break
            else:
                print("Número inválido. Debe estar entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    for i in range(num_monedas):

        # Paso 1: Ingresa nombre
        criptoName = input("Ingrese el nombre de la moneda (btc, bcc, ltc, eth, etc): ")

        # Validar nombre de la criptomoneda
        if getCripto(criptoName):
            break
        print("Moneda no válida. Intente nuevamente.")


    # Paso 2: Ingresar cantidad
    while True:
        cantidad = input(f"Ingrese cantidad de {criptoName}: ")

        # Validar cantidad
        if isNumber(cantidad):
            cantidad = float(cantidad)
            break
        print("Cantidad inválida. Debe ser un número.")

    # Paso 3: Ingresar valor    
    while True:
        valor = input(f"Ingrese el valor de {criptoName} en USD: ")

        # Validar valor
        if isNumber(valor):
            valor = float(valor)
            break
        print("Valor inválido. Debe ser un número.")

    # Agregar a listas
    criptos.append(criptoName)
    cantidades.append(cantidad)
    valores.append(valor)

    # Mostrar resumen
    mostrarResumen(criptos, cantidades, valores)

# Funcion ejecutadora del programa
def main():

    print("\n" + "="*50)
    print(" REGISTRO DE CRIPTOMONEDAS ".center(50, '='))
    print("="*50)
    cargarMonedas()

# Inicializador del programa
if __name__ == "__main__":
    main()

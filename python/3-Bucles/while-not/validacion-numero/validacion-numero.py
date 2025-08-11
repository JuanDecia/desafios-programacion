# Cada Función tiene una sola responsabilidad

# Solicita un número al usuario
def solicitar_numero():
    return input("Ingrese un número: ")

# Valida la entrada del usuario
def validar_numero(entrada):
    return entrada.isdigit()

# Funcion principal, maneja el flujo del programa
def main():

    # Recibe el número ingresado
    numeroUsuario = solicitar_numero()

    # Valida la entrada del usuario
    # Si no es un número, solicita nuevamente
    while not validar_numero(numeroUsuario):
        print("❌ No se reconoció el número ingresado. Intente nuevamente.")
        numeroUsuario = solicitar_numero()

    numeroValidado = int(numeroUsuario)
    print(f"✅ Número aceptado: {numeroValidado}")

# Inicia el programa
if __name__ == "__main__":
    main()
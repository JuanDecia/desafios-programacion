# Solicitar numero al usuario
def solicitarNumero() -> int:

# Valida el número ingresado por el usuario
        while True:            
            try:
                return int(input("Ingrese un número: "))
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")

# FizzBuzz
def fizzBuzz(numero: int) -> str:

    if numero % 3 == 0 and numero % 5 == 0:
        return ("FizzBuzz")
    elif numero % 3 == 0:
        return ("Fizz")
    elif numero % 5 == 0:
        return ("Buzz")
    else:
        return str(numero)

# Función principal
def main():
    numeroUsuario = solicitarNumero()
    resultado = fizzBuzz(numeroUsuario)
    print(f"El resultado de FizzBuzz para el número {numeroUsuario} es: {resultado}")

# Ejecución del programa
if __name__ == "__main__":
    main()